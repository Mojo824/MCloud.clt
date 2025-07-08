import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

def list_key_pairs():
    response = ec2.describe_key_pairs()
    return response.get('KeyPairs', [])

def show_key_pairs(key_pairs):
    if not key_pairs:
        print("No key pairs found.")
        return
    for idx, kp in enumerate(key_pairs, 1):
        print(f"{idx}. {kp['KeyName']}")

def delete_key_pair(key_name):
    try:
        ec2.delete_key_pair(KeyName=key_name)
        print(f"Deleted key pair {key_name}")
    except ClientError as e:
        print(f"Failed to delete {key_name}: {e}")

key_pairs = list_key_pairs()
show_key_pairs(key_pairs)

if not key_pairs:
    exit()

print("\nEnter the numbers of the key pairs to delete (e.g., 1,3,5), or 'all' to delete all:")
choice = input("Your choice: ").strip().lower()

if choice == 'all':
    for kp in key_pairs:
        delete_key_pair(kp['KeyName'])
else:
    try:
        indices = [int(x.strip()) for x in choice.split(',') if x.strip().isdigit()]
        for idx in indices:
            if 1 <= idx <= len(key_pairs):
                delete_key_pair(key_pairs[idx-1]['KeyName'])
            else:
                print(f"Invalid selection: {idx}")
    except Exception as e:
        print(f"Invalid input: {e}")
