import json
import boto3
import os
from datetime import datetime, timedelta

def lambda_handler(event, context):
    
    access_key = os.environ["aws_access_key_id"]
    secret_access_key = os.environ["aws_secret_access_key"]
    db = boto3.client('dynamodb', aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key, region_name='us-east-2')
    
    shortlink = event["queryStringParameters"]["shortlink"]
    data = db.get_item(TableName='pastes', Key={'shortlink': {'S': shortlink}},
        AttributesToGet=['paste_path', 'created_at', 
                         'expiration_length_in_minutes'])
        
    if 'Item' not in data:
        return {'statusCode': 400, 'body': json.dumps({"content": ""})}
        
    paste_path = data['Item']['paste_path']['S']
    created_at = datetime.strptime(data['Item']['created_at']['S'],
        '%Y-%m-%d %H:%M')
    expiration_length = int(data['Item']['expiration_length_in_minutes']['N'])
    expires_at = created_at + timedelta(minutes=expiration_length)
        
    # load file from s3
    bs, bucket, path = paste_path.split('/')
    s3 = boto3.resource('s3', aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key, region_name='us-east-2')
    bkt = s3.Bucket('sd-pastebin-pastes')
    bkt.download_file(path, '/tmp/{}'.format(path))
    with open('/tmp/{}'.format(path)) as f:
        paste_contents = f.read()
        
    # return paste_contents
    return {'statusCode': 200, 'body': json.dumps({
        "paste_contents": paste_contents,
        "created_at": created_at.strftime('%Y-%m-%d %H:%M'),
        "expires_at": expires_at.strftime('%Y-%m-%d %H:%M')
    })}
