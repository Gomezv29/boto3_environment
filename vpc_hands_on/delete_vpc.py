import boto3

vpc_id = 'vpc-01143858d90013a1d'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)


