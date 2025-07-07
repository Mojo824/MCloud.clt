import boto3
from botocore.exceptions import ClientError

region = input("Enter AWS region (e.g., us-east-1): ")

def list_ebs_volumes(region):
    ec2 = boto3.client('ec2', region_name=region)
    volumes = ec2.describe_volumes()['Volumes']
    return volumes

def show_volumes(volumes):
    if not volumes:
        print("No EBS volumes found.")
        return
    for idx, vol in enumerate(volumes, 1):
        state = vol['State']
        attachments = vol['Attachments']
        attached = 'Yes' if attachments else 'No'
        print(f"{idx}. VolumeId: {vol['VolumeId']} | State: {state} | Attached: {attached}")

def delete_volume(region, volume_id):
    ec2 = boto3.client('ec2', region_name=region)
    try:
        vol = ec2.describe_volumes(VolumeIds=[volume_id])['Volumes'][0]
        if vol['Attachments']:
            print(f"ERROR: Volume {volume_id} is attached to an instance. Skipping.")
            return
        ec2.delete_volume(VolumeId=volume_id)
        print(f"Deleted volume {volume_id}")
    except ClientError as e:
        print(f"Failed to delete {volume_id}: {e}")

def delete_all_in_all_regions():
    ec2 = boto3.client('ec2')
    regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]
    for reg in regions:
        print(f"\nRegion: {reg}")
        volumes = list_ebs_volumes(reg)
        for vol in volumes:
            delete_volume(reg, vol['VolumeId'])

volumes = list_ebs_volumes(region)
show_volumes(volumes)

if not volumes:
    exit()

print("\nEnter the numbers of the EBS volumes to delete (e.g., 1,3,5), 'all' to delete all in this region, or 'all-regions' to delete all in all regions:")
choice = input("Your choice: ").strip().lower()

if choice == 'all':
    for vol in volumes:
        delete_volume(region, vol['VolumeId'])
elif choice == 'all-regions':
    delete_all_in_all_regions()
else:
    try:
        indices = [int(x.strip()) for x in choice.split(',') if x.strip().isdigit()]
        for idx in indices:
            if 1 <= idx <= len(volumes):
                delete_volume(region, volumes[idx-1]['VolumeId'])
            else:
                print(f"Invalid selection: {idx}")
    except Exception as e:
        print(f"Invalid input: {e}")
