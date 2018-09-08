koodo-notifier
==============

[![Build Status](https://travis-ci.org/zehengl/koodo-notifier.svg?branch=master)](https://travis-ci.org/zehengl/koodo-notifier)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

An SMS notifier for Koodo usage

Prerequiste
-----------
Assuming you have access the following services
* A Koodo account
* A github account
* An aws account (SNS delivers the text message)
* A rollbar account (lazy error tracking)
* A Travis CI account (daily cron job)


Setup
-----
### aws
1. Create an IAM with programmatic access user for SNS resource, if it doesn't exist already
2. Markdown the access key and secret key

### rollbar
1. Create a new project
2. Markdown the rollbal key

### github
1. Fork this repo

### Travis CI
1. Enable build on Travis CI
2. Set the environment variables on Travis CI
	- aws: access_key / secret_key
	- rollbar: rollbar_key
	- Koodo: username(email) / password
3. Set a daily cron job

All set!

You should get a daily text message like the one below.

![example](https://github.com/zehengl/koodo-notifier/blob/master/example.jpg)
