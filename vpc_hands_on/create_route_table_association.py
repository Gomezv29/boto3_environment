import boto3

route_table_id = 'rtb-0ae46ff95404a8e1c'
subnet_id = 'subnet-01f706946cdb2a4c8'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationID"])