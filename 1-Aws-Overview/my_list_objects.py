import boto3

client = boto3.client('s3')
response = client.list_objects(Bucket='rumdevbucket')

for content in response['Contents']:
	obj_dict = client.get_object(Bucket='rumdevbucket', Key=content['Key'])
	print(content['Key'], content['Size'])
