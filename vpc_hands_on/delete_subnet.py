import boto3

subnet_id = 'subnet-0740be244bc8a1109'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)

