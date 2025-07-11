import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def list_buckets():
    response = s3.list_buckets()
    return response.get('Buckets', [])

def show_buckets(buckets):
    if not buckets:
        print("No S3 buckets found.")
        return
    for idx, bucket in enumerate(buckets, 1):
        print(f"{idx}. {bucket['Name']}")

def delete_bucket(bucket_name):
    try:
        # First, try to delete all objects in the bucket
        s3_resource = boto3.resource('s3')
        bucket = s3_resource.Bucket(bucket_name)
        bucket.objects.all().delete()
        # Now delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Deleted bucket {bucket_name}")
    except ClientError as e:
        print(f"Failed to delete {bucket_name}: {e}")

buckets = list_buckets()
show_buckets(buckets)

if not buckets:
    exit()

print("\nEnter the numbers of the S3 buckets to delete (e.g., 1,3,5), or 'all' to delete all:")
choice = input("Your choice: ").strip().lower()

if choice == 'all':
    confirm = input("Are you sure you want to delete ALL buckets? (yes/no): ").strip().lower()
    if confirm in ('yes', 'y'):
        for bucket in buckets:
            confirm2 = input(f"Confirm delete bucket '{bucket['Name']}'? (yes/no): ").strip().lower()
            if confirm2 in ('yes', 'y'):
                delete_bucket(bucket['Name'])
            else:
                print(f"Skipped {bucket['Name']}")
    else:
        print("Operation cancelled.")
else:
    try:
        indices = [int(x.strip()) for x in choice.split(',') if x.strip().isdigit()]
        for idx in indices:
            if 1 <= idx <= len(buckets):
                bucket_name = buckets[idx-1]['Name']
                confirm = input(f"Are you sure you want to delete bucket '{bucket_name}'? (yes/no): ").strip().lower()
                if confirm in ('yes', 'y'):
                    delete_bucket(bucket_name)
                else:
                    print(f"Skipped {bucket_name}")
            else:
                print(f"Invalid selection: {idx}")
    except Exception as e:
        print(f"Invalid input: {e}")
