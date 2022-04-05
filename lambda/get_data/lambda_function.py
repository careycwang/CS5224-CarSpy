import json
import boto3
from time import gmtime, strftime
from botocore.exceptions import ClientError
from pprint import pprint
from boto3.dynamodb.conditions import Key
from recommendation import recommend
from select_data import get_cars
from get_history import get_history
dynamodb = boto3.resource('dynamodb')

now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('current-user')
    response = table.scan(
                FilterExpression=Key('id').eq("current-user"),
                ProjectionExpression="userid"
            )
    
    userid = response["Items"][0]["userid"]
    pprint(userid)
    if not "brand" in event.keys(): # default 
        cars = get_cars()
    else:
        cars = get_cars(event["brand"], event["model"], event["year_range"], event["price_range"], dynamodb)
    if event["recommend"] == True:  # based on user's view history
        if event["history"] == True:
            view_history, star_history = get_history(userid)
            if len(star_history) > 0:
                cars = recommend(cars, star_history[-1], num_recommendation=5)
            elif len(view_history) > 0:
                cars = recommend(cars, view_history[-1], num_recommendation=5)
            else: # no star_history or view_history
                # cars = recommend(cars,  num_recommendation=5)
                cars = sorted(cars, key = lambda x: (x["stared"], x["viewed"]), reverse=True)[:5]
        else:                       # based on popularity
            cars = recommend(cars,  num_recommendation=5)
    else:                           
        # pprint(cars)
        cars = sorted(cars, key = lambda x: (x["stared"], x["viewed"]), reverse=True)[:5]
    if cars:
        return {
            'statusCode': 200,
            'body': json.dumps(cars)
            # 'body': json.dumps(event['headers'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('No item found!')
        }
    