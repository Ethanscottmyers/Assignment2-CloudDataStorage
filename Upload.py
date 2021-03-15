import boto3
import csv

s3 = boto3.resource(
    's3', 
    aws_access_key_id='', 
    aws_secret_access_key=''
)

db = boto3.resource(
    'dynamodb',
    region_name='us-west-2',
    aws_access_key_id='', 
    aws_secret_access_key=''
)

try: 
    table = db.Table('DataTable')
except Exception as e2:
    print(e2)

with open(r'C:\Users\ethan\Documents\Pitt\Spring 2021\Cloud Computing\Assignments\Assignment 2\Assignment2-CloudDataStorage\Example\experiments.csv', 'r') as csvfile:
    csvf = csv.reader(csvfile, delimiter=',')
    next(csvf) #skip header row
    for item in csvf:
        body = open(r'C:\Users\ethan\Documents\Pitt\Spring 2021\Cloud Computing\Assignments\Assignment 2\Assignment2-CloudDataStorage\Example\\' + item[4], 'rb')
        s3.Object('etm36assignmenttwo', item[4]).put(Body=body)
        md = s3.Object('etm36assignmenttwo', item[4]).Acl().put(ACL='public-read')
        url = 'https://etm36assignmenttwo.s3-us-west-2.amazonaws.com/' + item[4]
        metadata_item = {
            'partition': item[0],
            'itemid': item[1],
            'date': item[2],
            'comment': item[3],
            'url': url
        }
        try:
            table.put_item(Item=metadata_item)
        except Exception as e:
            print(e)
