#!/bin/bash -e

if [[ -z "$NEW_RELIC_LICENSE_KEY" ]]; then
  echo "ERROR: env var NEW_RELIC_LICENSE_KEY not provided" >&2
  exit 1
fi

export NEW_RELIC_CONFIG_FILE=./newrelic.ini

if [[ -f $NEW_RELIC_CONFIG_FILE ]]; then
#  newrelic-admin run-program celery -A tasks worker --loglevel=debug
  celery worker -A tasks --concurrency=1 --loglevel=debug -n localhost
fi
