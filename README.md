# koodo-notifier

[![Build Status](https://travis-ci.org/zehengl/koodo-notifier.svg?branch=master)](https://travis-ci.org/zehengl/koodo-notifier)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![time tracker](https://wakatime.com/badge/github/zehengl/koodo-notifier.svg)](https://wakatime.com/badge/github/zehengl/koodo-notifier)

A Koodomobile usage notifier, with a similar idea to [rrfortune](https://github.com/zehengl/rrfortune)

## Prerequisites

Assuming you have access the following services

- A Koodo account
- A GitHub account
- An AWS account (SNS delivers the text message)
- A Rollbar account (lazy error tracking)
- A Travis CI account (daily cron job)

## Setup

### AWS

1. Create an IAM with programmatic access user for SNS resource, if it doesn't exist already
2. Markdown the access key and secret key

### Rollbar

1. Create a new project
2. Markdown the access token (rollbar key)

### GitHub

1. Fork this repo

### Travis CI

1. Enable build on Travis CI
2. Set the environment variables on Travis CI
   - AWS: access_key / secret_key
   - Rollbar: rollbar_key
   - Koodo: username(email) / password
3. Set a daily cron job

All set!

You should get a daily text message like the one below.

![example](https://github.com/zehengl/koodo-notifier/blob/master/example.jpg)

## Develop

Setup chromedriver

    curl -O https://chromedriver.storage.googleapis.com/2.46/chromedriver_mac64.zip
    unzip -o chromedriver_mac64.zip
    mv -f chromedriver /usr/local/bin/chromedriver

Export credentials

    export username="..."
    export password="..."
    export access_key="..."
    export secret_key="..."
    export rollbar_key="..."

Run test

    cd koodo-notifier
    python -m venv venv
    source venv/bin/activate
    pip install -U pip
    pip install -r requirements-dev.txt
    pytest
