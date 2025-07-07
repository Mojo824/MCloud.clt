
import boto3
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ServiceawsDM import fakeload
# ec2 = boto3.client("ec2")
# ec2_resource = boto3.resource("ec2")

# # Common OS names and their AMI mappings (region specific )
# ami_map = {
#     "ubuntu": "ami-080e1f13689e07408",   # Ubuntu Server 22.04 LTS (example)
#     "amazon-linux": "ami-0c2b8ca1dad447f8a",  # Amazon Linux 2
#     "debian": "ami-00a6eeb43b1f9f96b",    # Debian (example)
#     "centos": "ami-0d63de463e6604d0a",    # CentOS 7 (example)
#     "redhat": "ami-052c08d70def0ac62"     # RHEL 8 (example)
# }

# print("Supported OS options:")
# for os_name in ami_map:
#     print(f"- {os_name}")

# chosen_os = input("Enter the OS you want (e.g., ubuntu, amazon-linux): ").strip().lower()
# if chosen_os not in ami_map:
#     print("Unsupported OS. Exiting...")
#     exit(1)

# ami_id = ami_map[chosen_os]

# # Key Pair
# key_pairs = ec2.describe_key_pairs()["KeyPairs"]
# existing_keys = [kp["KeyName"] for kp in key_pairs]

# print("\nAvailable Key Pairs:")
# for i, key in enumerate(existing_keys, 1):
#     print(f"{i}. {key}")

# key_name = input("\nEnter an existing key pair name or a new one to create: ").strip()
# if key_name not in existing_keys:
#     print(f"Creating new key pair '{key_name}'...")
#     key_pair = ec2.create_key_pair(KeyName=key_name)
#     with open(f"{key_name}.pem", "w") as file:
#         file.write(key_pair["KeyMaterial"])
#     print(f"Key pair saved to {key_name}.pem (Make sure to change its permission: chmod 400)")
# else:
#     print(f"Using existing key pair: {key_name}")

# # Security group
# print("\nSecurity Group: Using default security group.")
# print(" To create or modify security groups, go to the 'Networking' section of MCloud.")

# # Instance Type
# instance_types = [
#     "t2.micro", "t3.micro", "t3a.micro",
#     "t2.small", "t3.small", "t2.medium", "t3.medium",
#     "m5.large", "c5.large", "a1.medium"
# ]

# print("\nChoose an instance type:")
# for i, itype in enumerate(instance_types, 1):
#     print(f"{i}. {itype}")

# try:
#     choice = int(input("Your choice: ")) - 1
#     instance_type = instance_types[choice] if 0 <= choice < len(instance_types) else "t2.micro"
# except:
#     print("Invalid choice, using default 't2.micro'")
#     instance_type = "t2.micro"

# # Launch Instance
# print("\nLaunching EC2 instance...")
# response = ec2.run_instances(
#     ImageId=ami_id,
#     InstanceType=instance_type,
#     KeyName=key_name,
#     MinCount=1,
#     MaxCount=1,
#     SecurityGroups=['default']
# )

# instance_id = response["Instances"][0]["InstanceId"]
# print(f" Waiting for instance {instance_id} to enter 'running' state...")

# ec2_resource = boto3.resource("ec2", region_name=region)
# instance = ec2_resource.Instance(instance_id)
# instance.wait_until_running()

# instance.load()
# public_ip = instance.public_ip_address

# print("\n EC2 Instance launched successfully!")
# print(f"Instance ID: {instance_id}")
# print(f"Public IP: {public_ip}")
# print(f"State: {instance.state['Name']}")
# print(f"Launch Time: {instance.launch_time}")
# print(f"Type: {instance.instance_type}")
# print(f"AMI: {instance.image_id}")
# print(f"Key Pair: {instance.key_name}")

# # Asking  about static website hosting
# host_website = input("\n Do you want to host a static website on this instance? (y/n): ").strip().lower()
# if host_website == "y":
#     print(" Redirecting to static website setup...")
# else:
#     print(" Setup complete. You can now SSH into your instance and deploy your applications.")



#Chatgpt ka code (Niche) tha 2 ghnte phle
#ab mera hogya 


# Get default region from config

session = boto3.session.Session()
region = session.region_name

if not region:
    print(" !! No region configured. Please run 'aws configure' first.")
    exit(1)
    

ec2 = session.client("ec2")
ec2_resource = session.resource("ec2")

ami_map_by_region = {
    "us-east-1": {  #Virginia (lgbtq+)
        "ubuntu": "ami-0fc5d935ebf8bc3bc",
        "amazon-linux": "ami-0c101f26f147fa7fd",
        "debian": "ami-033b95fb8079dc481",
        "rhel": "ami-0aeeebd8d2ab47354",
        "windows": "ami-03c7c4b1c6d9c6c63"
    },
    "ap-south-1": {  #Mumbai(chal htt bkl))
        "ubuntu": "ami-0f58b397bc5c1f2e8",
        "amazon-linux": "ami-03f4878755434977f",
        "debian": "ami-099b1ebd8c5e99e4b",
        "rhel": "ami-087ecf9ce5d35c82e",
        "windows": "ami-04f5098988d6f8b1f"
    },
    "eu-west-1": { #Ireland (go raibh maith agat)
        "ubuntu": "ami-01dd271720c1ba44f",
        "amazon-linux": "ami-050a61c8a6df1c8fe",
        "debian": "ami-0fdb4e6586fdc52d8",
        "rhel": "ami-0a8c10f2a82f27c4a",
        "windows": "ami-0867b0e17e8bb41f6"
    },
    "ap-northeast-1": { #Tokyo (Aarigato)
        "ubuntu": "ami-0310483fb2b488153",
        "amazon-linux": "ami-0d52744d6551d851e",
        "debian": "ami-0fcb5b064298f3dba",
        "rhel": "ami-0b2f6494ff0b07d10",
        "windows": "ami-0a3f10e6f1f6de43d"
    },
    "sa-east-1": {
        "ubuntu": "ami-0f2c95c3f9c933d41",
        "amazon-linux": "ami-04e0a32b8b4e4e2fb",
        "debian": "ami-07b98ecf61c2b03f4",
        "rhel": "ami-02658c4c4a9c2a6ff",
        "windows": "ami-0035ddbd72b297f7a"
    }
    # here edit here 
} 


if region not in ami_map_by_region:
    print(f"❌ Region '{region}' not supported in AMI map. You can Edit the code at MCloud/Aws/Compute/Deployec2 and can add your region Or just wait for Future updates :)")
    exit(1)

print ("                    +++Ec3 Deploy Tool MCloud  +++ ")
print(f"\n Using region: {region}")
print("\nSupported OS options for your region:")
ami_map = ami_map_by_region[region]
for os_name, ami_id in ami_map.items():
    print(f"- {os_name}: {ami_id}")

chosen_os = input("\nEnter the OS you want (e.g., ubuntu, amazon-linux): ").strip().lower()
if chosen_os not in ami_map:
    print("Unsupported OS. Exiting...")
    exit(1)

ami_id = ami_map[chosen_os]

# Key Pair
try :
    key_pairs = ec2.describe_key_pairs()["KeyPairs"]
    existing_keys = [kp["KeyName"] for kp in key_pairs]
except Exception as e :
    print (e + "\n Check for the permisssions ")

print("\nAvailable Key Pairs:")
for i, key in enumerate(existing_keys, 1):
    print(f"{i}. {key}")

key_name = input("\nEnter an existing key pair name or a new one to create: ").strip()
if key_name not in existing_keys:
    print(f"Creating new key pair '{key_name}'...")
    key_pair = ec2.create_key_pair(KeyName=key_name)
    with open(f"{key_name}.pem", "w") as file:
        file.write(key_pair["KeyMaterial"])
    print(f"Key pair saved to {key_name}.pem (chmod 400 recommended)")
else:
    print(f"Using existing key pair: {key_name}")

# Security group
print("\nSecurity Group: Using default security group.")
print(" To create or modify security groups, go to the 'Networking' section of MCloud.")

# Instance Type
instance_types = [
    "t2.micro",
    "t3.micro",
    "t3a.micro",
    "t2.small",
    "t3.small",
    "t2.medium",
    "t3.medium",
    "m5.large",
    "c5.large",
    "a1.medium"
]

# Suggetion 
print ("\n[*] Choose an instance type (Like write their num 1 or 2 ..etc ): \n"
        '\n1. t2.micro [Free Tier : 1 GB RAM, 1 vCPU, EBS ],'
        '\n2. t3.micro [Maybe Free IDK : 1 GB RAM, 2 vCPU (burstable), EBS ],'
        '\n3. t3a.micro [General Purpose : 1 GB RAM, 2 vCPU (burstable), EBS ],'
        '\n4. t2.small [General Purpose : 2 GB RAM, 1 vCPU, EBS ],'
        '\n5. t3.small [General Purpose : 2 GB RAM, 2 vCPU (burstable), EBS ],'
        '\n6. t2.medium [General Purpose : 4 GB RAM, 2 vCPU, EBS ],'
        '\n7. t3.medium [General Purpose : 4 GB RAM, 2 vCPU (burstable), EBS ],'
        '\n8. m5.large [Compute Optimized : 8 GB RAM, 2 vCPU, EBS ],'
        '\n9. c5.large [Compute Optimized : 4 GB RAM, 2 vCPU, EBS ],'
        '\n10. a1.medium [ARM-based : 2 GB RAM, 1 vCPU , EBS ]'
        )

try:
    choice = int(input("\n EBS means it doesn't come with local instance storage.\n [*] t2/t3/t3a series are burstable (means : search yourself )  performance instances.\n [*] t2.micro is the **only confirmed** Free Tier eligible instance (check for t3.micro in your Region).\n Your choice (by num eg. 1 or 2 or etc): ")) - 1
    instance_type = instance_types[choice] if 0 <= choice < len(instance_types) else "t2.micro"
except:
    print("Invalid choice, using default 't2.micro'")
    instance_type = "t2.micro"

# Launch Instance
print("\n Launching EC2 instance...")
# Get first available Subnet ID
subnets = ec2.describe_subnets()
subnet_id = subnets['Subnets'][0]['SubnetId'] if subnets['Subnets'] else None

# Get first available Security Group ID
security_groups = ec2.describe_security_groups()
sg_id = security_groups['SecurityGroups'][0]['GroupId'] if security_groups['SecurityGroups'] else None

if not subnet_id or not sg_id:
    print("❌ Could not find a valid subnet or security group.")
    exit(1)

print(f"Using Subnet ID: {subnet_id}")
print(f"Using Security Group ID: {sg_id}")

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    MinCount=1,
    MaxCount=1,
    NetworkInterfaces=[
        {
            'DeviceIndex': 0,
            'SubnetId': subnet_id,
            'Groups': [sg_id],
            'AssociatePublicIpAddress': True
        }
    ]

)

instance_id = response["Instances"][0]["InstanceId"]
print(f" [$] Waiting for instance {instance_id} to enter 'running' state...")

instance = ec2_resource.Instance(instance_id)
instance.wait_until_running()
instance.load()

public_ip = instance.public_ip_address

print("\n EC2 Instance launched successfully!")
print(f"Instance ID: {instance_id}")
print(f"Public IP: {public_ip}")
print(f"State: {instance.state['Name']}")
print(f"Launch Time: {instance.launch_time}")
print(f"Type: {instance.instance_type}")
print(f"AMI: {instance.image_id}")
print(f"Key Pair: {instance.key_name}")

# Asking about static website hosting
# host_website = input("\n Do you want to host a static website on this instance? (y/n): ").strip().lower()
# if host_website == "y":
#     print(" Redirecting to static website setup...")
#     fakeload(" Web Hosting")
#     print (" Feature coming soon ...")
# else:
print("🎉 Setup complete. You can now SSH into your instance and deploy your applications.")
