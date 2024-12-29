import boto3

internet_gateway_id = 'igw-0b021a77cfb2c1d04'
vpc_id = 'vpc-0004bf5a5c89eceb7'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)


