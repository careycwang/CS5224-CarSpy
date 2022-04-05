from botocore.exceptions import ClientError
import json
import boto3
from time import gmtime, strftime
from pprint import pprint
from boto3.dynamodb.conditions import Key

def get_cars(brand=None, model=None, year_range=None, price_range=None, dynamodb=None):
    if dynamodb == None:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('carspy-table-03')
    try:
        if brand == None:
            pprint(1)
            response = table.scan(
                FilterExpression=Key('year').between("2008", "2010"),
                ProjectionExpression="#id, #br, model, price, transmission, mileage, mpg, fuelType, engineSize, #yr, pca_1, pca_2, viewed, stared",
                ExpressionAttributeNames={"#br": "brand", "#yr": "year", "#id": "uuid"}
            )
            
        else:
            response = table.scan(
                FilterExpression=Key('brand').eq(brand) & Key('model').eq(model) & Key('year').between(str(year_range[0]), str(year_range[1])) & Key('price').between(str(price_range[0]), str(price_range[1])),
                ProjectionExpression="#id, #br, model, price, transmission, mileage, mpg, fuelType, engineSize, #yr, pca_1, pca_2, viewed, stared",
                ExpressionAttributeNames={"#br": "brand", "#yr": "year", "#id": "uuid"}
            )
        # response = table.get_item(Key={'brand':brand, 'model':model})
        # pprint(response)
    except ClientError as e:
        pprint(e.response['Error']['Message'])
    else:
        return response['Items']