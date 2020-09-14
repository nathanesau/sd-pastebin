# lambda functions

Code is provided for the AWS lambda functions.

## Instructions

To create the lambda functions:

* copy the code from ``lambda_function.py``, etc. to the appropriate folder.
* set the ``aws_access_key_id`` and ``aws_secret_access_key`` environment variables in the lambda.

To create the api gateway (which calls the lambda functions):

* add ``readPaste`` (GET) and ``writePaste`` (POST) routes to the api gateway.
* configure CORS (Access-Control-Allow-Origin to ``*``, Access-Control-Allow-Headers to ``content-type``, Access-Control-Allow-Methods to ``*``, Access-Control-Expose-Headers to ``content-type``).