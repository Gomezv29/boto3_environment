import boto3

vpc_id = 'vpc-0004bf5a5c89eceb7'

ec2 = boto3.client('ec2')

response = ec2.create_route_table(VpcId=vpc_id)

print(response["RouteTable"]["RouteTableId"])
