# System Design - Pastebin

Simple implementation of Pastebin. This repository will be helpful for those wishing to learn more about system design.

Based on suggestions in https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md.

Site should be live at: https://nathanesau.github.io/sd-pastebin/

## Technical Info 

I have taken a serverless approach.

* The api endpoints are written using Python (AWS lambda).
* Paste metadata is stored in DynamoDB (``pastes`` table with ``shortlink (String)`` partition key).
* Pastse are stored in S3 blob storage (``sd-pastebin-pastes`` bucket).

Some advantages of this design:

* Cheap (AWS lambda and DynamoDB are free up to certain limit and S3 is relatively cheap since I am not storing much data).
* Don't need to manage any servers
* Don't need to manage database (creating schema, sharding, replicas, etc.)

Some disadvtanges:

* It is a little slow since I am not using a cache.
* With a cache, we reduce amount of DynamoDB and S3 read/writes which is faster.
* Redis cache or memcached cache could be used, but it costs more money (RAM is relatively expensive).

## AWS Notes

For AWS lambda to be able to access DynamoDB and S3, IAM role was created (``aws_access_key_id`` and ``aws_secret_access_key``). Each of the lambda functions set these environment variables and use the ``boto3`` Python package to connect to the services.

A lot can be done with just this set of tools (API - AWS Lambda, API Gateway, Database - DynamoDB, BlobStore - S3).

## Additional Notes

Frontend is written using vue.js and deployed to ``gh-pages``.

The api is publicly accessible, so anyone who knows what the url is could access the API directly. If this is a concern, the website could be a private repository (so people can't see the api calls in the javascript code). Or another alternative is to use environment variables for API links and put the website in AWS as well.

## Design

![](basic_design.png)
