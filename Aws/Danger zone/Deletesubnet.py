import boto3
from botocore.exceptions import ClientError

region = input("Enter AWS region (e.g., us-east-1): ")

def list_subnets(region):
    ec2 = boto3.client('ec2', region_name=region)
    subnets = ec2.describe_subnets()['Subnets']
    return subnets

def show_subnets(subnets):
    if not subnets:
        print("No subnets found.")
        return
    for idx, subnet in enumerate(subnets, 1):
        subnet_id = subnet['SubnetId']
        vpc_id = subnet['VpcId']
        cidr = subnet['CidrBlock']
        state = subnet['State']
        print(f"{idx}. SubnetId: {subnet_id} | VpcId: {vpc_id} | CIDR: {cidr} | State: {state}")

def subnet_in_use(subnet):
    # AWS does not provide a direct 'in use' flag, but if available IPs is 0, it's likely in use
    return subnet['AvailableIpAddressCount'] == 0

def delete_subnet(region, subnet):
    if subnet_in_use(subnet):
        print(f"ERROR: Subnet {subnet['SubnetId']} appears to be in use. Skipping.")
        return
    ec2 = boto3.client('ec2', region_name=region)
    try:
        ec2.delete_subnet(SubnetId=subnet['SubnetId'])
        print(f"Deleted Subnet {subnet['SubnetId']}")
    except ClientError as e:
        print(f"Failed to delete {subnet['SubnetId']}: {e}")

def delete_all_in_all_regions():
    ec2 = boto3.client('ec2')
    regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]
    for reg in regions:
        print(f"\nRegion: {reg}")
        subnets = list_subnets(reg)
        for subnet in subnets:
            delete_subnet(reg, subnet)

subnets = list_subnets(region)
show_subnets(subnets)

if not subnets:
    exit()

print("\nEnter the numbers of the subnets to delete (e.g., 1,3,5), 'all' to delete all in this region, or 'all-regions' to delete all in all regions:")
choice = input("Your choice: ").strip().lower()

if choice == 'all':
    for subnet in subnets:
        delete_subnet(region, subnet)
elif choice == 'all-regions':
    delete_all_in_all_regions()
else:
    try:
        indices = [int(x.strip()) for x in choice.split(',') if x.strip().isdigit()]
        for idx in indices:
            if 1 <= idx <= len(subnets):
                subnet = subnets[idx-1]
                delete_subnet(region, subnet)
            else:
                print(f"Invalid selection: {idx}")
    except Exception as e:
        print(f"Invalid input: {e}")
