import boto3

internet_gateway_id = 'igw-0213f07d275e74bbb'
vpc_id = 'vpc-01143858d90013a1d'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)


