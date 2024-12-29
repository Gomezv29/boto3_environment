import boto3

route_table_id = 'rtb-0342e1bdef9af6e1a'

ec2 = boto3.client('ec2')

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id,
)


# Creation route
# VPC
#    Subnet
#      Route Table
#        Associating Route Table with Subnet
#             Internet Gateway
#                 Attaching Internet Gateway to Route Table


# Deletion Route
# Delete association between Internet Gateway and Route Table
#     Internet Gateway
#           Delete association between Route Table and Subnet
#                Route Table
#                    Subnet
#                        VPC