import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2',region_name='us-west-2') ,
    response = client.run_instances(
    ImageId='ami-035bf26fb18e75d1b',
    MaxCount=1,
    MinCount=1,
    InstanceType='t2.micro' ,
    KeyName = 'i3'

)
