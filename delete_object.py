import boto3
from list_objects import list_object_keys

def delete_object(client, bucket, key):
    response = client.delete_object(
    Bucket=bucket,
    Key=key,
)

    return response

def delete_objects(client, bucket, keys):
    objects = [{'Key': key,} for key in keys]
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects':objects
        }
)

    return response

if __name__ == '__main__':
    bucket = 'vgomez-boto3-12242024'
    s3 = boto3.client('s3')
    
    
    keys = list_object_keys(s3, bucket, prefix="folder")
    delete_objects(s3, bucket, keys)