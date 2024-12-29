import boto3

route_table_id = 'rtb-0342e1bdef9af6e1a'

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)

