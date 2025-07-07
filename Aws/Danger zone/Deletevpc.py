import boto3
from botocore.exceptions import ClientError

region = input("Enter AWS region (e.g., us-east-1): ")

def list_vpcs(region):
    ec2 = boto3.client('ec2', region_name=region)
    vpcs = ec2.describe_vpcs()['Vpcs']
    return vpcs

def show_vpcs(vpcs):
    if not vpcs:
        print("No VPCs found.")
        return
    for idx, vpc in enumerate(vpcs, 1):
        vpc_id = vpc['VpcId']
        cidr = vpc['CidrBlock']
        print(f"{idx}. VpcId: {vpc_id} | CIDR: {cidr}")

def vpc_has_subnets(region, vpc_id):
    ec2 = boto3.client('ec2', region_name=region)
    subnets = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])['Subnets']
    return len(subnets) > 0

def delete_vpc(region, vpc_id):
    if vpc_has_subnets(region, vpc_id):
        print(f"ERROR: VPC {vpc_id} has subnets attached. Skipping.")
        return
    ec2 = boto3.client('ec2', region_name=region)
    try:
        ec2.delete_vpc(VpcId=vpc_id)
        print(f"Deleted VPC {vpc_id}")
    except ClientError as e:
        print(f"Failed to delete {vpc_id}: {e}")

def delete_all_in_all_regions():
    ec2 = boto3.client('ec2')
    regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]
    for reg in regions:
        print(f"\nRegion: {reg}")
        vpcs = list_vpcs(reg)
        for vpc in vpcs:
            delete_vpc(reg, vpc['VpcId'])

vpcs = list_vpcs(region)
show_vpcs(vpcs)

if not vpcs:
    exit()

print("\nEnter the numbers of the VPCs to delete (e.g., 1,3,5), 'all' to delete all in this region, or 'all-regions' to delete all in all regions:")
choice = input("Your choice: ").strip().lower()

if choice == 'all':
    for vpc in vpcs:
        delete_vpc(region, vpc['VpcId'])
elif choice == 'all-regions':
    delete_all_in_all_regions()
else:
    try:
        indices = [int(x.strip()) for x in choice.split(',') if x.strip().isdigit()]
        for idx in indices:
            if 1 <= idx <= len(vpcs):
                vpc = vpcs[idx-1]
                delete_vpc(region, vpc['VpcId'])
            else:
                print(f"Invalid selection: {idx}")
    except Exception as e:
        print(f"Invalid input: {e}")
