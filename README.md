This is a clean-room implementation of a "hello world" celery app that reports to NewRelic.

## Status ##

ALPHA. Not guaranteed to work in your environment. YMMV.

## Audience ##

Python Celery users who would like to see their performance stats in NewRelic dashboard.
This tutorial is written for experienced software developers, with the assumption of Linux knowledge.

## How to use ##

1. clone this repo
2. on your dev machine or another machine resource, set up a development purpose `rabbitmq-server`, accepting default port, and (roughly) with these config steps:
    - `sudo rabbitmqctl add_vhost demo`
    - `sudo rabbitmqctl add_user guest:guest`
    - `sudo rabbitmqctl set_permissions -p demo guest ".*" ".*" ".*"`
    - `sudo rabbitmqctl stop && rabbitmq-server -detached # restarting the rabbitmq server`
3. `source .env` to bootstrap the virtualenv and pip requirements (`autoenv` is recommended to consume this file automatically)
4. `./run_worker.sh`, the script should start up, ending with the message `consumer: Ready to accept tasks!`
5. `./client.py -i` to enter interactive mode as a caller of async tasks.
6. `export NEW_RELIC_LICENSE_KEY=<your account license key>` if you'd like to integrate with NewRelic APM
