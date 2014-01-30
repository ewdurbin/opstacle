
opstacle
========

An SMTP proxy built around [inbox.py](https://github.com/kennethreitz/inbox.py)
which attempts to maintain some sanity as your servers begin to send thousands
of emails just cause.

Configuration
-------------

opstacle is configured only by environment variables, and our contestants are:

- OPSTACLE_FROM_ADDRESS
  - Sample Value: "Opstacle <opstacle@opstacle.io>"
- OPSTACLE_SMTP_USER
  - Sample Value: "postmaster@smtp.opstacle.org"
- OPSTACLE_SMTP_PASS
  - Sample Value: "stopTheInsanity"
- OPSTACLE_SMTP_HOST
  - Sample Value: "smtp.opstacle.org"
- OPSTACLE_SMTP_PORT
  - Sample Value: "587"
- OPSTACLE_MESSAGE_CAP
  - Sample Value: 5
- OPSTACLE_INTERVAL
  - Sample Value: 30
- OPSTACLE_LISTEN_HOST
  - Sample Value: "127.0.0.1"
- OPSTACLE_LISTEN_PORT
  - Sample Value: 9025

Running
-------

Once installed, opstacle can be invoked by calling `opstacle`.

Logs are spit directly to YOU! Right there on STDOUT, and no you can't turn them down
