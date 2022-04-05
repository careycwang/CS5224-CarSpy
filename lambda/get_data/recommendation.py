from botocore.exceptions import ClientError
import json
import boto3
from time import gmtime, strftime
from pprint import pprint
from boto3.dynamodb.conditions import Key
import numpy as np

def recommend(cars, item_id="db8af34a-e09e-346b-b404-1a29aededec5", num_recommendation=5):
    """
    A simple recommender system using PCA
    """
    pprint(item_id)
    # feature_vectors = pca.fit_transform(data_dummies)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('carspy-table-03')
    response = table.scan(
                FilterExpression=Key('uuid').eq(item_id),
                ProjectionExpression="pca_1, pca_2"
            )
    target_feature_vector = response['Items'][0]
    target_feature_vector = [float(target_feature_vector['pca_1']), float(target_feature_vector['pca_2'])]
    # pprint(target_feature_vector)
    feature_vectors = np.array([[float(car['pca_1']), float(car['pca_2'])] for car in cars])
    # pprint(feature_vectors)
    # distances = []
    # for feature_vector in feature_vectors:
    #     distances.append(np.sum(feature_vector - feature_vectors[item_id,:])**2)
    # distances = np.sum((feature_vectors - feature_vectors[item_id,:])**2, axis=1)
    distances = np.sum((feature_vectors - target_feature_vector)**2, axis = 1)
    rec_ids = np.argsort(distances)[1:1+num_recommendation]
    # pprint(rec_ids)
    rec_desc = [cars[rec_id] for rec_id in rec_ids]
    pprint('You have viewed:\n')
    # pprint(f'Id: {item_id} | Product: {cars[item_id]}')
    pprint('\n\nWe recommend:\n')
    res = []
    for i, d in zip(rec_ids, rec_desc):
        res.append(d)
        pprint(f'Id: {i} | Product: {d}')
    return res
