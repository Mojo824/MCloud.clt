import boto3
import time
def allocate_elastic_ip():
    print(" Allocate an Elastic IP (EIP)")

    region = input("Enter AWS region [default: us-east-1]: ") or "us-east-1"
    eip_type = input("Choose EIP type - 1. Standard (default)  2. Global Accelerator: ")

    domain = "vpc" if eip_type.strip() != "2" else "global"

    # Optional tags
    tag_input = input("Add tags? (key1=value1,key2=value2) or leave blank: ").strip()
    tags = []
    if tag_input:
        try:
            for item in tag_input.split(","):
                key, value = item.split("=")
                tags.append({"Key": key.strip(), "Value": value.strip()})
        except Exception:
            print(" Invalid tag format. Skipping tags.")

    ec2 = boto3.client("ec2", region_name=region)

    try:
        response = ec2.allocate_address(Domain=domain)
        allocation_id = response.get("AllocationId")
        public_ip = response.get("PublicIp")

        if tags and allocation_id:
            ec2.create_tags(Resources=[allocation_id], Tags=tags)

        print("\n Elastic IP allocated successfully!")
        print(f"Public IP       : {public_ip}")
        print(f"Allocation ID   : {allocation_id}")
        print(f"Domain          : {domain}")
        if tags:
            print(f"Tags            : {tags}")
        print(f"Region          : {region}")

    except Exception as e:
        print("❌ Error allocating EIP:", e)

if __name__ == "__main__":
    print ("                      +++ Elastic ip  Tool MCloud +++")
    time.sleep(2)
    allocate_elastic_ip()