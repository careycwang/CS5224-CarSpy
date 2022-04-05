from botocore.exceptions import ClientError
import json
import boto3
from time import gmtime, strftime
from pprint import pprint
from boto3.dynamodb.conditions import Key

def get_history(userid="abcdevfefe-1232132-cofevf"):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user_info_2')
    try:
        response = table.scan(
            FilterExpression=Key('id').eq(userid),
            ProjectionExpression="view_history, star_history"
        )
        pprint(response)
    except ClientError as e:
        pprint(e.response['Error']['Message'])
    else:
        return response['Items'][0]["view_history"], response['Items'][0]["star_history"]