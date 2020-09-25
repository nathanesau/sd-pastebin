# System Design - Pastebin

Simple implementation of Pastebin. This repository will be helpful for those wishing to learn more about system design. I have written a simple REST api in flask and provided a few docker commands for spinning up a postgres database and redis cache. The frontend is a vue.js application.

The background scheduler for expiring old content is part of the flask application.

Based on suggestions in https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md.

Site should be live at: https://nathanesau.github.io/sd-pastebin/

## Design

![](basic_design.png)

## Technical Info 

I have taken a serverless approach.

* The api endpoints are written using Python (AWS lambda).
* Paste metadata is stored in DynamoDB (``pastes`` table with ``shortlink (String)`` partition key).
* Pastse are stored in S3 blob storage (``sd-pastebin-pastes`` bucket).

Some advantages of this design:

## Deploy Instructions

1. Set environment variables (see ``pastebin-backend/deploy/README.md``).

2. Run ``pastebin-backend/deploy/master/deploy.sh`` or ``pastebin-backend/deploy/slave/deploy.sh``. That script builds the docker images and brings up the images. It also brings up linux services if applicable.

To check status of docker containers use ``docker ps``.

To check status of linux service use ``systemctl status <service>``.
