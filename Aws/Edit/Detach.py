import boto3
import os

def list_attached_volumes(ec2_resource):
    print("\n Searching for attached EBS volumes...")
    volumes = ec2_resource.volumes.all()
    attached_volumes = []
    for vol in volumes:
        for attachment in vol.attachments:
            if attachment['State'] == 'attached':
                attached_volumes.append({
                    'VolumeId': vol.id,
                    'InstanceId': attachment['InstanceId'],
                    'Device': attachment['Device'],
                    'AZ': vol.availability_zone
                })
    if not attached_volumes:
        print("❌ No attached volumes found.")
        return None
    for i, v in enumerate(attached_volumes, 1):
        print(f"{i}. Volume ID: {v['VolumeId']}, Instance ID: {v['InstanceId']}, Device: {v['Device']}, AZ: {v['AZ']}")
    return attached_volumes

def main():
    region = input("Enter AWS region [default: us-east-1]: ") or "us-east-1"
    ec2 = boto3.client("ec2", region_name=region)
    ec2_resource = boto3.resource("ec2", region_name=region)

    attached_volumes = list_attached_volumes(ec2_resource)
    if not attached_volumes:
        return

    try:
        vol_choice = int(input("Choose volume index to detach: ")) - 1
        selected = attached_volumes[vol_choice]
    except:
        print("❌ Invalid selection. Exiting.")
        return

    volume_id = selected['VolumeId']
    instance_id = selected['InstanceId']
    device = selected['Device']

    confirm = input(f"Are you sure you want to detach {volume_id} from {instance_id}? (y/n): ").lower()
    if confirm != 'y':
        print("❌ Detach operation cancelled.")
        return

    force = input("Force detach? (y/n): ").lower() == 'y'

    try:
        ec2.detach_volume(VolumeId=volume_id, InstanceId=instance_id, Device=device, Force=force)
        print(f" Detach request sent for Volume {volume_id} from Instance {instance_id} (force={force}).")
    except Exception as e:
        print("❌ Error detaching volume:", e)
        return

    delete = input("Do you want to delete this volume after detaching? (y/n): ").lower()
    if delete == 'y':
        try:
            print(" Waiting for volume to be 'available' before deletion...")
            volume = ec2_resource.Volume(volume_id)
            volume.wait_until_available()
            ec2.delete_volume(VolumeId=volume_id)
            print(" Volume deleted successfully.")
        except Exception as e:
            print("❌ Error deleting volume:", e)

if __name__ == "__main__":
    main()