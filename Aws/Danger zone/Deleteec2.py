import boto3
from botocore.exceptions import ClientError

region = input("Enter AWS region (e.g., us-east-1): ")

def list_ec2_instances(region):
    ec2 = boto3.client('ec2', region_name=region)
    reservations = ec2.describe_instances()['Reservations']
    instances = []
    for res in reservations:
        for inst in res['Instances']:
            instances.append(inst)
    return instances

def show_instances(instances):
    if not instances:
        print("No EC2 instances found.")
        return
    for idx, inst in enumerate(instances, 1):
        state = inst['State']['Name']
        instance_id = inst['InstanceId']
        name = next((tag['Value'] for tag in inst.get('Tags', []) if tag['Key'] == 'Name'), 'N/A')
        print(f"{idx}. InstanceId: {instance_id} | Name: {name} | State: {state}")

def terminate_instance(region, instance_id, state):
    if state not in ['running', 'stopped']:
        print(f"ERROR: Instance {instance_id} is in state '{state}' and cannot be terminated. Skipping.")
        return
    ec2 = boto3.client('ec2', region_name=region)
    try:
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Terminated instance {instance_id}")
    except ClientError as e:
        print(f"Failed to terminate {instance_id}: {e}")

def terminate_all_in_all_regions():
    ec2 = boto3.client('ec2')
    regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]
    for reg in regions:
        print(f"\nRegion: {reg}")
        instances = list_ec2_instances(reg)
        for inst in instances:
            terminate_instance(reg, inst['InstanceId'], inst['State']['Name'])

instances = list_ec2_instances(region)
show_instances(instances)

if not instances:
    exit()

print("\nEnter the numbers of the EC2 instances to terminate (e.g., 1,3,5), 'all' to terminate all in this region, or 'all-regions' to terminate all in all regions:")
choice = input("Your choice: ").strip().lower()

if choice == 'all':
    for inst in instances:
        terminate_instance(region, inst['InstanceId'], inst['State']['Name'])
elif choice == 'all-regions':
    terminate_all_in_all_regions()
else:
    try:
        indices = [int(x.strip()) for x in choice.split(',') if x.strip().isdigit()]
        for idx in indices:
            if 1 <= idx <= len(instances):
                inst = instances[idx-1]
                terminate_instance(region, inst['InstanceId'], inst['State']['Name'])
            else:
                print(f"Invalid selection: {idx}")
    except Exception as e:
        print(f"Invalid input: {e}")
