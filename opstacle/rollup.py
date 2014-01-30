
from inbox import Inbox, InboxServer
from logbook import Logger

from util import ExpireCounter
from config import Config

from smtplib import SMTP
from email.mime.text import MIMEText

import asyncore
import threading

import time
from collections import defaultdict, deque

config = Config()
log = Logger(__name__)

class RecipientStore(object):

    def __init__(self, timeout=30):
        self.messages = deque()
        self.counter = ExpireCounter(timeout=timeout)

    def __len__(self):
        return len(self.messages)

    def add_message(self, message=None):
        self.messages.append(message)

    def incr_counter(self):
        self.counter.add('message')

    def clear_messages(self):
        self.messages = deque()

    def backlog(self, to_addr):
        msg = MIMEText("\n".join(self.messages))
        msg['Subject'] = "Opstacle caught %s more messages" % (len(self.messages))
        msg['From'] = config.FROM_ADDRESS
        msg['To'] = to_addr
        return msg.as_string()

class RollUp(object):

    def __init__(self, messages=5, interval=30, auto_purge=100):
        self.recipients = defaultdict(RecipientStore)
        self.messages = messages
        self.interval = interval
        self.auto_purge = auto_purge
        self.smtp = SMTP(config.SMTP_HOST, int(config.SMTP_PORT))
        self.smtp.login(config.SMTP_USER, config.SMTP_PASS)

    def send(self, msg_from, msg_to, msg_body):
        self.smtp.sendmail(msg_from, msg_to, msg_body)

    def purge(self, force=False):
        for poor_bastard in self.recipients:
            recip = self.recipients[poor_bastard]

            if len(recip.counter) > self.messages and len(recip.messages) < self.auto_purge:
                if not force:
                    return

            if len(recip) > 0:
                log.info("purging to %s" % (poor_bastard))
                self.send(config.FROM_ADDRESS, poor_bastard, recip.backlog(poor_bastard))
                recip.clear_messages()

    def rollup_handler(self, to, sender, body):
        for poor_bastard in to:
            recip = self.recipients[poor_bastard]

            recip.incr_counter()

            if len(recip.counter) > self.messages:
                recip.add_message(body)
                if len(recip.counter) < self.auto_purge:
                    log.info('throttling to %s' % (poor_bastard))
                else:
                    log.info('auto purging to %s' % (poor_bastard))
                    self.purge()
                return

            log.info('sending to %s' % (poor_bastard))
            self.send(sender, to, body)


class RollUpPurger(threading.Thread):
    daemon = True

    def __init__(self, rollup=None):
        threading.Thread.__init__(self)
        self.rollup = rollup

    def run(self, rollup=None):
        while True:
            if self.rollup:
                self.rollup.purge()
            time.sleep(30)


class RollUpInbox(Inbox):

    def __init__(self):
        super(RollUpInbox, self).__init__()
        self.rollup = RollUp(messages=config.MESSAGE_CAP, interval=config.MESSAGE_INTERVAL,
                             auto_purge=config.AUTO_PURGE)
        self.collator = self.rollup.rollup_handler

    def serve(self, port=None, address=None):
        """Serves the SMTP server on the given port and address."""
        port = port or self.port
        address = address or self.address

        log.info('Starting SMTP server at {0}:{1}'.format(address, port))

        server = InboxServer(self.collator, (address, port), None)

        purger = RollUpPurger(rollup=self.rollup)
        purger.start()

        try:
            while True:
                asyncore.loop()
        except KeyboardInterrupt:
            self.rollup.purge(force=True)
            self.rollup.smtp.quit()
            log.info('Cleaning up')
