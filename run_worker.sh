#!/bin/bash -e

if [[ -z "$NEW_RELIC_LICENSE_KEY" ]]; then
  echo "ERROR: env var NEW_RELIC_LICENSE_KEY not provided" >&2
  exit 1
fi

export NEW_RELIC_CONFIG_FILE=./newrelic.ini
export CELERY_TRACE_APP=1

if [[ -f $NEW_RELIC_CONFIG_FILE ]]; then
  celery_worker_args="--app=tasks.my_app --concurrency=1 --loglevel=debug"
  celery worker $celery_worker_args
# newrelic-admin run-program celery -A tasks worker --loglevel=debug
fi
