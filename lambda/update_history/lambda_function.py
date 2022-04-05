from __future__ import print_function
import boto3
from pprint import pprint
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    
    # 
    car_table = dynamodb.Table('carspy-table-03')
    # Return to Amazon Cognito
    car_id = event["uuid"]
    if event["history"] == "viewed":
        
        response = car_table.scan(
                FilterExpression=Key('uuid').eq(car_id),
                ProjectionExpression="viewed"
            )
    
        viewed_num = response["Items"][0]["viewed"]
        viewed_num = str(int(viewed_num) + 1)
        
        response = car_table.update_item(
            Key={
                'uuid': car_id,
            },
            UpdateExpression="set viewed = :val",
            ExpressionAttributeValues={
                ':val': viewed_num
            },
            ReturnValues="UPDATED_NEW"
        )
    if event["history"] == "stared-1": # add stared
        response = car_table.scan(
                FilterExpression=Key('uuid').eq(car_id),
                ProjectionExpression="stared"
            )
    
        stared_num = response["Items"][0]["stared"]
        stared_num = str(int(stared_num) + 1)
        
        response = car_table.update_item(
            Key={
                'uuid': car_id,
            },
            UpdateExpression="set stared = :val",
            ExpressionAttributeValues={
                ':val': stared_num
            },
            ReturnValues="UPDATED_NEW"
        )
    
    if event["history"] == "stared-0": # remove stared
        response = car_table.scan(
                FilterExpression=Key('uuid').eq(car_id),
                ProjectionExpression="stared"
            )
    
        stared_num = response["Items"][0]["stared"]
        stared_num = str(int(stared_num) - 1)
        
        response = car_table.update_item(
            Key={
                'uuid': car_id,
            },
            UpdateExpression="set stared = :val",
            ExpressionAttributeValues={
                ':val': stared_num
            },
            ReturnValues="UPDATED_NEW"
        )
    cur_user_table = dynamodb.Table('current-user')
    response = cur_user_table.scan(
                FilterExpression=Key('id').eq("current-user"),
                ProjectionExpression="userid"
            )
    
    userid = response["Items"][0]["userid"]
    pprint(userid)
    
    user_table = dynamodb.Table('user_info_2')
    # Return to Amazon Cognito

    if event["history"] == "viewed":
        response = user_table.update_item(
            Key={
                'id': userid,
            },
            UpdateExpression="set #v = list_append(#v, :val)",
            ExpressionAttributeNames={
                "#v": "view_history",
            },
            ExpressionAttributeValues={
                ":val": [car_id]
            },
            ReturnValues="UPDATED_NEW"
        )
    if event["history"] == "stared-":
        response = user_table.update_item(
            Key={
                'id': userid,
            },
            UpdateExpression="set #s = list_append(#s, :val)",
            ExpressionAttributeNames={
                "#s": "star_history",
            },
            ExpressionAttributeValues={
                ":val": [car_id]
            },
            ReturnValues="UPDATED_NEW"
        )
    
    return response
    # return event['userName']
