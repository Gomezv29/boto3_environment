import boto3

def filter_objects_extension(client, bucket, extension):
    keys = []
    response = client.list_objects_v2(Bucket=bucket) 
    for content in response["Contents"]:
        if(extension in content["Key"][-(len(extension)):]):
            keys.append(content["Key"])
    return keys
    

def list_object_keys(client, bucket, prefix=""):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix) 
    for content in response["Contents"]:
            keys.append(content["Key"])
    return keys

if __name__ == '__main__':
    s3 = boto3.client('s3') 

# for api's always use the latest version documented on the documentation pages

#response = s3.list_objects_v2(Bucket="vgomez-boto3-12242024") #Prefix="folderhere") will list anything nested under the folder named

    response = list_object_keys(s3, "vgomez-boto3-12242024",)

    response = filter_objects_extension(s3, "vgomez-boto3-12242024", ".txt")

#extension = ".txt"

    print(response)
