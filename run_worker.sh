#!/bin/bash -e

if [[ -z "$NEW_RELIC_LICENSE_KEY" ]]; then
  echo "WARN: env var NEW_RELIC_LICENSE_KEY not provided" >&2
fi

export NEW_RELIC_CONFIG_FILE=./newrelic.ini
# export CELERY_TRACE_APP=1

if [[ -f $NEW_RELIC_CONFIG_FILE ]]; then
  celery_worker_args="--app=tasks.my_app --concurrency=1 --loglevel=debug"
  if [[ -n "$NEW_RELIC_LICENSE_KEY" ]]; then
    echo "INFO: running with NewRelic monitoring"
    newrelic-admin run-program celery worker $celery_worker_args
  else
    echo "WARN: running without NewRelic monitoring" >&2
    celery worker $celery_worker_args
  fi
fi
