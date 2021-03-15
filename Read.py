import boto3

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

response = table.get_item(
    Key={
        'partition': 'experiment1',
        'itemid': 'data1'
    }
)
print(response['Item'])