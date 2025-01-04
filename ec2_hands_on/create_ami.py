import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
   
    Description='An AMI for my server',
    InstanceId='i-0f6ca0d4237faa6fd',
    Name='Go to Ami'
)

print(response["ImageId"])