import boto3
import csv

s3 = boto3.resource(
    's3', 
    aws_access_key_id='', 
    aws_secret_access_key=''
)

# try: 
#     s3.create_bucket(Bucket='etm36assignmenttwo', CreateBucketConfiguration={
#         'LocationConstraint': 'us-west-2'
#     })
# except:
#     print('this bucket may already exist')

bucket = s3.Bucket('etm36assignmenttwo')
bucket.Acl().put(ACL='public-read')

# body = open('Example\experiments.csv', 'rb')
# o = s3.Object('etm36assignmenttwo', 'test').put(Body=body)
# s3.Object('etm36assignmenttwo', 'test').Acl().put(ACL='public-read')

db = boto3.resource(
    'dynamodb',
    region_name='us-west-2',
    aws_access_key_id='', 
    aws_secret_access_key=''
)

try:
    table = db.create_table(
        TableName='DataTable',
        KeySchema=[
            {
                'AttributeName': 'partition',
                'KeyType': 'HASH'
            }, 
            {
                'AttributeName': 'itemid', 
                'KeyType': 'RANGE'
            }
        ], 
        AttributeDefinitions=[
            {
                'AttributeName': 'partition',
                'AttributeType': 'S'
            }, 
            {
                'AttributeName': 'itemid',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
except Exception as e:
    try: 
        table = db.Table('DataTable')
    except Exception as e2:
        print(e2)


