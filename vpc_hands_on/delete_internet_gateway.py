import boto3

internet_gateway_id = 'igw-0213f07d275e74bbb'

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)
