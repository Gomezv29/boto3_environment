import boto3

ec2 = boto3.client('ec2')

vpc = ec2.create_vpc(CidrBlock='12.0.0.0/17')

print(vpc["Vpc"]["VpcId"])

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