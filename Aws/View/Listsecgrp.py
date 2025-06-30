import boto3
import time 
def get_all_regions():
    ec2 = boto3.client("ec2")
    return [r["RegionName"] for r in ec2.describe_regions()["Regions"]]

def show_regions_menu(regions):
    print("\nAvailable AWS Regions:")
    for idx, region in enumerate(regions):
        print(f"{idx + 1}. {region}")
    print("a. All regions")

def get_user_region_selection(regions):
    selection = input("\nEnter region index(es) (e.g., 1 or 1,3 or 'a' for all): ").strip().lower()
    if selection == 'a':
        return regions

    try:
        indexes = [int(i.strip()) - 1 for i in selection.split(',')]
        return [regions[i] for i in indexes if 0 <= i < len(regions)]
    except ValueError:
        print("❌ Invalid input.")
        return []

def get_vpc_name(vpcs, vpc_id):
    vpc = vpcs.get(vpc_id)
    if not vpc:
        return "N/A"
    for tag in vpc.get("Tags", []):
        if tag["Key"].lower() == "name":
            return tag["Value"]
    return "N/A"

def print_rules(rules):
    if not rules:
        print("   ❌ No rules defined.")
        return
    for rule in rules:
        proto = rule.get("IpProtocol", "all")
        from_port = rule.get("FromPort", "all")
        to_port = rule.get("ToPort", "all")
        ip_ranges = [ip['CidrIp'] for ip in rule.get("IpRanges", [])]
        desc = rule.get("Description", "")
        print(f"   🔸 Protocol: {proto}, Ports: {from_port}-{to_port}, CIDRs: {ip_ranges or 'N/A'}")

def list_security_groups_in_region(region):
    print(f"\nRegion: {region}")
    print("-" * 60)
    
    ec2 = boto3.client("ec2", region_name=region)

    try:
        sgs = ec2.describe_security_groups()["SecurityGroups"]
        vpcs = {v["VpcId"]: v for v in ec2.describe_vpcs()["Vpcs"]}
    except Exception as e:
        print(f"Error: {e}")
        return

    if not sgs:
        print("❌ No security groups found.")
        return

    for sg in sgs:
        sg_id = sg["GroupId"]
        name = sg.get("GroupName", "N/A")
        vpc_id = sg.get("VpcId", "N/A")
        vpc_name = get_vpc_name(vpcs, vpc_id)

        print(f"Security Group : {name}")
        print(f"SG ID          : {sg_id}")
        print(f"VPC            : {vpc_id} ({vpc_name})")

        print(" Inbound Rules:")
        print_rules(sg.get("IpPermissions", []))

        print(" Outbound Rules:")
        print_rules(sg.get("IpPermissionsEgress", []))

        print("-" * 60)

def main():
    regions = get_all_regions()
    show_regions_menu(regions)

    selected_regions = get_user_region_selection(regions)
    if not selected_regions:
        print("❌ No valid regions selected.")
        return

    for region in selected_regions:
        list_security_groups_in_region(region)

if __name__ == "__main__":
    print ("                    +++ List Security Group Tool MCloud +++")
    time.sleep(1)
    while True:
        main()
        again=input ("\n Wanna see Others or Again (y/n): ").strip().lower()
        if again!="y":
            break
