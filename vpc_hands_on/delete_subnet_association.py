import boto3

route_table_id = 'rtb-0342e1bdef9af6e1a'

ec2 = boto3.client('ec2')

# association_id = ''   Cannot be found in the console

response = ec2.describe_route_tables(
    RouteTableIds=[
        route_table_id,
    ],
)

for association in response["RouteTables"][0]["Associations"]:
    if not association["Main"]:
        association_id = association["RouteTableAssociationId"]
        print(association_id)
        ec2.disassociate_route_table(
            AssociationId=association_id,
        )

# Just like in creation you can find the documentation under:
# ec2 documents
#     'disassociate_route_table'