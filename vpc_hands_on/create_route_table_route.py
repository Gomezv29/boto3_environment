import boto3

route_table_id = 'rtb-0342e1bdef9af6e1a'
internet_gateway_id = 'igw-0213f07d275e74bbb'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)


