from __future__ import print_function
import boto3
def lambda_handler(event, context):
    
    print ("Authentication successful")
    print ("Trigger function =", event['triggerSource'])
    print ("User pool = ", event['userPoolId'])
    print ("App client ID = ", event['callerContext']['clientId'])
    print ("User ID = ", event['userName'])

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('current-user')
    # Return to Amazon Cognito
    id = "current-user"
    response = table.update_item(
        Key={
            'id': id,
        },
        UpdateExpression="set userid = :val",
        ExpressionAttributeValues={
            ':val': event['userName']
        },
        ReturnValues="UPDATED_NEW"
    )
    return event
    # return event['userName']
