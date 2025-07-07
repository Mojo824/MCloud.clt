import boto3
import os
from pathlib import Path

base_dir= Path(__file__)
parent_dir= base_dir.parent.parent
febs_dir= parent_dir/'Storage'/'Deployeebs.py'
fec2_dir = parent_dir/'Compute'/'Deployec2.py'


def list_available_volumes(ec2):
    print("\n Searching for available EBS volumes...")
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])['Volumes']
    if not volumes:
        print("❌ No available volumes found.")
        return None
    for i, vol in enumerate(volumes, 1):
        print(f"{i}. Volume ID: {vol['VolumeId']}, Size: {vol['Size']}GB, AZ: {vol['AvailabilityZone']}")
    return volumes

def list_running_instances(ec2_resource):
    print("\n Searching for running EC2 instances...")
    instances = list(ec2_resource.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]))
    if not instances:
        print(" ❌ No running EC2 instances found.")
        return None
    for i, inst in enumerate(instances, 1):
        name = next((tag['Value'] for tag in inst.tags or [] if tag['Key'] == 'Name'), 'N/A')
        print(f"{i}. Instance ID: {inst.id}, Name: {name}, AZ: {inst.placement['AvailabilityZone']}")
    return instances

def main():
    region = input("Enter AWS region [default: us-east-1]: ") or "us-east-1"
    ec2 = boto3.client("ec2", region_name=region)
    ec2_resource = boto3.resource("ec2", region_name=region)

    # Step 1: Check and list volumes
    volumes = list_available_volumes(ec2)
    if not volumes:
        choice = input("Do you want to deploy a new volume? (y/n): ").lower()
        if choice == 'y':
            os.system(f"python3 {febs_dir}")
            volumes = list_available_volumes(ec2)
            if not volumes:
                print("❌ No volume available after deploy. Exiting.")
                return
        else:
            return

    vol_choice = int(input("Choose volume index to attach: ")) - 1
    selected_vol = volumes[vol_choice]
    volume_id = selected_vol['VolumeId']
    vol_az = selected_vol['AvailabilityZone']

    # Step 2: Check and list instances
    instances = list_running_instances(ec2_resource)
    if not instances:
        choice = input("Do you want to deploy a new EC2 instance? (y/n): ").lower()
        if choice == 'y':
            os.system(f"python3{fec2_dir}" )
            instances = list_running_instances(ec2_resource)
            if not instances:
                print("❌ No instance found after deploy. Exiting.")
                return
        else:
            return

    inst_choice = int(input("Choose EC2 instance index to attach to: ")) - 1
    selected_inst = instances[inst_choice]
    instance_id = selected_inst.id
    inst_az = selected_inst.placement['AvailabilityZone']

    # Check AZ match
    if inst_az != vol_az:
        print(f"❌ Volume AZ ({vol_az}) and Instance AZ ({inst_az}) must match!")
        return

    device_name = input("Enter device name to attach (e.g. /dev/sdf) [default: /dev/sdf]: ") or "/dev/sdf"
    print(f"Attaching Volume {volume_id} to Instance {instance_id} as {device_name}...")

    try:
        ec2.attach_volume(VolumeId=volume_id, InstanceId=instance_id, Device=device_name)
        print(" Volume attached successfully.")
    except Exception as e:
        print("❌ Failed to attach volume:", e)

if __name__ == "__main__":
    main()