import boto3

route_table_id = 'rtb-0ae46ff95404a8e1c'
internet_gateway_id = 'igw-0b021a77cfb2c1d04'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)


