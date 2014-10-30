This is a clean-room implementation of a "hello world" celery app that reports to NewRelic.

## Status ##

ALPHA. Not guaranteed to work in your environment. YMMV.

#### disclaimer ####
- developed and tested only on OS X / VirtualBox hosted Vagrant machine (`precise64` box)
- NewRelic integration verified for `celery` version `3.0.25`, but not for `3.1.x` versions

## Audience ##

Python Celery users who would like to see their performance stats in NewRelic dashboard.
This tutorial is written for experienced software developers, with the assumption of Linux knowledge.

## How to use ##

1. clone this repo.
2. Install RabbitMQ server.
    `sudo apt-get install rabbitmq-server`
3. on your dev machine or another machine resource, set up a development purpose `rabbitmq-server`, accepting default port, and (roughly) with these config steps:
    - `sudo rabbitmqctl add_vhost demo`
    - `sudo rabbitmqctl add_user guest:guest` # This might not be necessary since apt-get install will setup ths user by default.
    - `sudo rabbitmqctl set_permissions -p demo guest ".*" ".*" ".*"`
    - `sudo rabbitmqctl stop` 
    - `sudo rabbitmq-server` -detached # restarting the rabbitmq server`
    - your setup steps may vary, proper rabbitmq admin is out of scope of this guide
4. `source .env` to bootstrap the virtualenv and pip requirements (`autoenv` is recommended to consume this file automatically)
5. `export NEW_RELIC_LICENSE_KEY=<your account license key>` if you'd like to integrate with NewRelic APM
6. `./run_worker.sh`, the script should start up, ending with the message `consumer: Ready to accept tasks!`
7. `./client.py -i` to enter interactive mode as a caller of async tasks.
