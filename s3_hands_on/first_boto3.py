import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket= 'vgomez-boto3-12242024'
)

print(response)

