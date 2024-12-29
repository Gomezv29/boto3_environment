import boto3

vpc_id = 'vpc-01143858d90013a1d'

ec2 = boto3.client('ec2')

response = ec2.create_route_table(VpcId=vpc_id)

print(response["RouteTable"]["RouteTableId"])
