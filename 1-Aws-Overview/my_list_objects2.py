import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('12291034-random-bucket')

for obj in bucket.objects.all():
	print(obj.key, obj.size)
