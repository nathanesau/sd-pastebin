# System Design - Pastebin

Simple implementation of Pastebin. This repository will be helpful for those wishing to learn more about system design. I have written a simple REST api in flask and provided a few docker commands for spinning up a postgres database and redis cache. The frontend is a vue.js application.

The background scheduler for expiring old content is part of the flask application.

Based on suggestions in https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md.

## Design

![](basic_design.png)

## Frontend

* Frontend written using ``vue.js`` (port 8080).

## Backend

* API written using ``flask`` (port 5000).
* Postgres database running using ``docker`` (port 5432).
* Redis cache running using ``docker`` (port 6379).

## Deploy Instructions

1. Set environment variables (see ``pastebin-backend/deploy/README.md``).

2. Run ``pastebin-backend/deploy/master/deploy.sh`` or ``pastebin-backend/deploy/slave/deploy.sh``. That script builds the docker images and brings up the images. It also brings up linux services if applicable.

To check status of docker containers use ``docker ps``.

To check status of linux service use ``systemctl status <service>``.