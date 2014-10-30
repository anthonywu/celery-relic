#!/bin/bash -e

source .env

if [[ -z "$NEW_RELIC_LICENSE_KEY" ]]; then
  echo "WARN: env var NEW_RELIC_LICENSE_KEY not provided" >&2
fi

export NEW_RELIC_CONFIG_FILE=./newrelic.ini

if [[ -f $NEW_RELIC_CONFIG_FILE ]]; then
  celery_worker_args="--app=tasks.my_app --concurrency=2 --loglevel=debug"
  if [[ -n "$NEW_RELIC_LICENSE_KEY" ]]; then
    echo "INFO: running with NewRelic monitoring"
    #newrelic-admin run-program celery worker $celery_worker_args
    newrelic-admin run-program celery multi start w1 w2 $celery_worker_args
  else
    echo "WARN: running without NewRelic monitoring" >&2
    #celery worker $celery_worker_args
    celery multi start w1 w2 $celery_worker_args
  fi
fi
