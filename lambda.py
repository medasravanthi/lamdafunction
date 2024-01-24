import boto3
import json

lambda_Client = boto3.client('lambda', region_name='us-west-2')
response = lambda_Client.create_function(
    Code={
        'S3Bucket': 's2-bucket.app',
        'S3Key': 'test.zip',  # how can i create or fetch this S3Key
    },

    FunctionName='lambda_s3',
    Handler='test.lambda_handler',
    Publish=True,
    Role= 'arn:aws:iam::660836083694:role/lambda-s3' ,
    Runtime='python3.12',
)
