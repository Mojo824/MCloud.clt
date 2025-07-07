import boto3
from botocore.exceptions import ClientError

region = input("Enter AWS region (e.g., us-east-1): ")

def list_security_groups(region):
    ec2 = boto3.client('ec2', region_name=region)
    groups = ec2.describe_security_groups()['SecurityGroups']
    # Exclude default security group
    return [g for g in groups if g['GroupName'] != 'default']

def show_security_groups(groups):
    if not groups:
        print("No security groups found (excluding default group).")
        return
    for idx, grp in enumerate(groups, 1):
        print(f"{idx}. GroupId: {grp['GroupId']} | GroupName: {grp['GroupName']} | Description: {grp['Description']}")

def delete_security_group(region, group_id):
    ec2 = boto3.client('ec2', region_name=region)
    try:
        ec2.delete_security_group(GroupId=group_id)
        print(f"Deleted security group {group_id}")
    except ClientError as e:
        print(f"Failed to delete {group_id}: {e}")

def delete_all_in_all_regions():
    ec2 = boto3.client('ec2')
    regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]
    for reg in regions:
        print(f"\nRegion: {reg}")
        groups = list_security_groups(reg)
        for grp in groups:
            delete_security_group(reg, grp['GroupId'])

groups = list_security_groups(region)
show_security_groups(groups)

if not groups:
    exit()

print("\nEnter the numbers of the security groups to delete (e.g., 1,3,5), 'all' to delete all in this region, or 'all-regions' to delete all in all regions:")
choice = input("Your choice: ").strip().lower()

if choice == 'all':
    for grp in groups:
        delete_security_group(region, grp['GroupId'])
elif choice == 'all-regions':
    delete_all_in_all_regions()
else:
    try:
        indices = [int(x.strip()) for x in choice.split(',') if x.strip().isdigit()]
        for idx in indices:
            if 1 <= idx <= len(groups):
                grp = groups[idx-1]
                delete_security_group(region, grp['GroupId'])
            else:
                print(f"Invalid selection: {idx}")
    except Exception as e:
        print(f"Invalid input: {e}")
