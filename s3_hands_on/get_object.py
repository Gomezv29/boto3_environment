import boto3

s3 = boto3.client('s3')
bucket = 'vgomez-boto3-12242024'
key = 'test_text_string.txt'

response = s3.get_object(Bucket=bucket, Key=key)

object_content = response['Body'].read()
contents= object_content.decode('utf-8')

print(contents)
