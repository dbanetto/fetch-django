# Fetch Django

[![Build Status](https://travis-ci.org/zyphrus/fetch-django.svg)](https://travis-ci.org/zyphrus/fetch-django) [![Coverage Status](https://coveralls.io/repos/zyphrus/fetch-django/badge.svg)](https://coveralls.io/r/zyphrus/fetch-django)

A Django powered Web UI for Fetcher

## Goal

To provide a web interface and an API for automating fetching various
weekly/monthly release media like podcasts or web series.

## Setting up

### Requirements

Python 3.4+, npm and bower

For general setup run `./setup.sh`

### Development

- install development `pip install -r requirements/dev.txt`

- Don't forget to update database `./manage.py migrate`

- run `./manage.py runserver`

After writing some code:

- run `test.sh` to just run the test suite
- run `coverage.sh` to get the coverage of the test suite, view the results by
  opening `htmlcov/index.html` in your browser

# Deploying

## [Dokku](https://github.com/dokku/dokku/)

* setup remote `git add remote dokku *user*@*hostname*:fetch`

* setup database on dokku `dokku postgres:create fetch_db`

* link it to the app `dokku postgres:link fetch_db fetch`

* deploy `git push dokku`

## License

Licensed under MIT, see LICENSE.md for more detail.

## Others Works

The files: down.png and down.svg in app/static are from [Numix Circle
icon pack](https://github.com/numixproject/numix-icon-theme-circle) system-software-install.svg
