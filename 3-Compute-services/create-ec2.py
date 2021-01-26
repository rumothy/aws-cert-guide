import boto3 # boto 3 is the AWS SDK for python
EC2 = boto3.client('ec2', region_name='us-east-2') # defines the EC2 variable which we will use in the lambda handler. We are defining the client as ec2 and the region as us-east-2.
def lambda_handler(event, context): 
    instance = EC2.run_instances(
        ImageId='ami-0d8f6eb4f641ef691',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        InstanceInitiatedShutdownBehavior='terminate'
    )
    instance_id = insance['Instances'][0]['InstanceId']
    print(instance_id)
    return instance_id