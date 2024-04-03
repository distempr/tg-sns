import boto3
import requests

ssm = boto3.client("ssm")

def lambda_handler(event, context):
    print(event)

#    token = ssm.get_parameter(
#        Name="/tg-sns/token",
#        WithDecryption=True
#    )["Parameter"]["Value"]
