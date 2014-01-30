
opstacle
========

An SMTP proxy built around [inbox.py](https://github.com/kennethreitz/inbox.py)
which attempts to maintain some sanity as your servers begin to send thousands
of emails just cause.

The basic premise is emails from a given server or process will happen, but all
1300 aren't really necessary right this instant. god forbid if you pay by the
smtp delivery.

Installation
------------

`pip install opstacle`

Configuration
-------------

opstacle is configured only by environment variables, and our contestants are:

## Pretty things

- `OPSTACLE_FROM_ADDRESS`
  - Most messages will be simply relayed without modification, but we need our own name when we send rolled up emails
  - Sample Value: "Opstacle <opstacle@opstacle.io>"

## Threshold configuration

- `OPSTACLE_INTERVAL`
  - Interval to keep counters when messages have been sent, in seconds
  - Sample Value: 30
- `OPSTACLE_MESSAGE_CAP`
  - Max number of messages to send in a given `OPSTACLE_INTERVAL`
  - Sample Value: 5


## "Fake" SMTP server (where opstacle will listen) 

- `OPSTACLE_LISTEN_HOST`
  - Sample Value: "127.0.0.1"
- `OPSTACLE_LISTEN_PORT`
  - Sample Value: 9025


## "Real" SMTP server

- `OPSTACLE_SMTP_USER`
  - Sample Value: "postmaster@smtp.opstacle.org"
- `OPSTACLE_SMTP_PASS`
  - Sample Value: "stopTheInsanity"
- `OPSTACLE_SMTP_HOST`
  - Sample Value: "smtp.opstacle.org"
- `OPSTACLE_SMTP_PORT`
  - Sample Value: "587"

Running
-------

Once installed, opstacle can be invoked by calling `opstacle`.

Logs are spit directly to YOU! Right there on STDOUT, and no you can't turn them down
