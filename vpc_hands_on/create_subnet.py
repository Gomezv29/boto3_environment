import boto3

cidr_block = '12.0.1.0/25'
vpc_id = 'vpc-01143858d90013a1d'

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id)

print(subnet["Subnet"]["SubnetId"])