import boto3

# This script connects an EC2 server to an S3 bucket to read data
s3 = boto3.client('s3')

# Configuration - Replace with your actual bucket name
bucket_name = 'yusuf-babystore-data-2026' 
file_key = 'test.txt'

try:
    # Pulling the file from the S3 "Vault"
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    content = response['Body'].read().decode('utf-8')

    print("--- Data retrieved from S3 ---")
    print(content)
except Exception as e:
    print(f"Error: {e}")
