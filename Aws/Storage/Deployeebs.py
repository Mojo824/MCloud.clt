import boto3
import time
def create_ebs_volume():
    
    print("                 +++ EBS Volume Deploy Tool MCloud +++")
    time.sleep(2)

    region = input("Enter AWS region [default: us-east-1]: ") or "us-east-1"

    # EBS volume types
    volume_types = [
        "gp2  General Purpose SSD (baseline 3 IOPS/GB)",
        "gp3  General Purpose SSD (better performance, lower cost)",
        "io1  Provisioned IOPS SSD",
        "io2  Next-gen Provisioned IOPS SSD",
        "sc1  Cold HDD (low cost, infrequent access)",
        "st1  Throughput Optimized HDD (frequent access)"
    ]
    volume_type_keys = ["gp2", "gp3", "io1", "io2", "sc1", "st1"]

    print("\nChoose EBS volume type:")
    for i, vt in enumerate(volume_types, 1):
        print(f"{i}. {vt}")

    try:
        vt_index = int(input("Your choice [1-6]: ")) - 1
        volume_type = volume_type_keys[vt_index] if 0 <= vt_index < len(volume_type_keys) else "gp2"
    except:
        print("Invalid choice, using default 'gp2'")
        volume_type = "gp2"

    size = input("Enter volume size in GB [default: 8]: ").strip() or "8"

    # Availability Zone
    ec2 = boto3.client("ec2", region_name=region)
    try:
        azs = ec2.describe_availability_zones()
        print("\nAvailable zones:")
        for i, az in enumerate(azs["AvailabilityZones"], 1):
            print(f"{i}. {az['ZoneName']}")
        az_choice = int(input("Choose availability zone index: ")) - 1
        az_name = azs["AvailabilityZones"][az_choice]["ZoneName"]
    except:
        print("Invalid choice or error getting AZs, using default")
        az_name = region + "a"

    # Tags  are optional in this 
    tag_input = input("Add tags? (key1=value1,key2=value2) or leave blank: ").strip()
    tags = []
    if tag_input:
        try:
            for item in tag_input.split(","):
                key, value = item.split("=")
                tags.append({"Key": key.strip(), "Value": value.strip()})
        except:
            print(" Invalid tag format. Skipping tags...")

    try:
        vol_args = {
            "AvailabilityZone": az_name,
            "Size": int(size),
            "VolumeType": volume_type
        }
        if tags:
            vol_args["TagSpecifications"] = [{
                "ResourceType": "volume",
                "Tags": tags
            }]

        response = ec2.create_volume(**vol_args)

        print("\n [*] EBS Volume created!")
        print(f"Volume ID       : {response['VolumeId']}")
        print(f"Size            : {response['Size']} GB")
        print(f"Type            : {response['VolumeType']}")
        print(f"AZ              : {response['AvailabilityZone']}")
        print(f"State           : {response['State']}")
        if tags:
            print(f"Tags            : {tags}")
        print(f"Region          : {region}")

    except Exception as e:
        print("❌ Error creating EBS volume:", e)

if __name__ == "__main__":
    create_ebs_volume()