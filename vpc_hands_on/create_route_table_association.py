import boto3

route_table_id = 'rtb-0342e1bdef9af6e1a'
subnet_id = 'subnet-0740be244bc8a1109'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])

# In the boto3 documentation you can find the code under:
#  ec2 documents
#        'associate_route_table'