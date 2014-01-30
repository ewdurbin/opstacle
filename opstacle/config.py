
import os

class Config(object):

    def __init__(self):
        self.FROM_ADDRESS     = os.environ.get('OPSTACLE_FROM_ADDRESS', 'rollup@opstacle.lol')
        self.SMTP_USER        = os.environ.get('OPSTACLE_SMTP_USER', 'postmaster')
        self.SMTP_PASS        = os.environ.get('OPSTACLE_SMTP_PASS', '')
        self.SMTP_HOST        = os.environ.get('OPSTACLE_SMTP_HOST', '127.0.0.1')
        self.SMTP_PORT        = int(os.environ.get('OPSTACLE_SMTP_PORT', 25))
        self.MESSAGE_CAP      = int(os.environ.get('OPSTACLE_MESSAGE_CAP', 5))
        self.MESSAGE_INTERVAL = int(os.environ.get('OPSTACLE_INTERVAL', 30))
        self.AUTO_PURGE       = int(os.environ.get('OPSTACLE_AUTO_PURGE', 100))
        self.LISTEN_HOST      = os.environ.get('OPSTACLE_LISTEN_HOST', '127.0.0.1')
        self.LISTEN_PORT      = int(os.environ.get('OPSTACLE_LISTEN_PORT', '9025'))
