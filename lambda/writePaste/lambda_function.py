import json
import boto3
import os
from datetime import datetime
from shortlink_generator import *

def lambda_handler(event, context):
    
    access_key = os.environ['aws_access_key_id']
    secret_access_key = os.environ['aws_secret_access_key']
    
    request_id = context.aws_request_id
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    db = boto3.client('dynamodb', aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key, region_name='us-east-2')
        
    s3 = boto3.resource('s3', aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key, region_name='us-east-2')
    
    body = json.loads(event["body"])
    paste_contents = body["paste_contents"]
    expiration_length_in_minutes = body["expiration_length_in_minutes"]
    
    shortlink = generate_url(request_id, timestamp)
    
    path = '{}.txt'.format(shortlink)
    with open('/tmp/{}'.format(path), 'w') as f:
        f.write(paste_contents)
    
    # upload file to s3
    bkt = s3.Bucket('sd-pastebin-pastes')
    bkt.upload_file('/tmp/{}'.format(path), path)
    paste_path = 'S3:/sd-pastebin-pastes/{}'.format(path)
    
    # create row in dynamodb
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M')
    db.put_item(TableName='pastes', Item={'shortlink': {'S': shortlink},
        'created_at': {'S': created_at},
        'expiration_length_in_minutes': {'N': expiration_length_in_minutes},
        'paste_path': {'S': paste_path}
    })
        
    return {
        'statusCode': 200,
        'body': json.dumps({"shortlink": shortlink})
    }
