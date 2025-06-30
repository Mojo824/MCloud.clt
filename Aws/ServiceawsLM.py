import os 
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ServiceawsDM import fakeload
base_dir = os.path.dirname(os.path.abspath(__file__))



def ec2():
    fakeload("Ec2 List")
    Listec2_script = os.path.join(base_dir, "View", "Listec2.py")
    os.system(f"python3 {Listec2_script}")

def subnet():
    fakeload("Subnet List")
    Listsubnet_script = os.path.join(base_dir, "View", "Listsubnet.py")
    os.system(f"python3 {Listsubnet_script}")

def security_group():
    fakeload("Security Group List")
    Listsecgrp_script = os.path.join(base_dir, "View", "Listsecgrp.py")
    os.system(f"python3 {Listsecgrp_script}")

def vpc():
    fakeload("Vpc List")
    Listvpc_script = os.path.join(base_dir, "View", "Listvpc.py")
    os.system(f"python3 {Listvpc_script}")

def rules():
    fakeload("IAM List")
    Listrule_script = os.path.join(base_dir, "View", "Listrule.py")
    os.system(f"python3 {Listrule_script}")

def s3():
    fakeload("S3 List")
    Lists3_script = os.path.join(base_dir, "View", "Lists3.py")
    os.system(f"python3 {Lists3_script}")

def exit_program():
    print("\n Exiting... Have a good day!")
    exit()

# Service menu dictionary
services = {
    "1": ("EC2", ec2),
    "2": ("Subnet", subnet),
    "3": ("Security Group", security_group),
    "4": ("VPC", vpc),
    #"5": ("Inbound/Outbound Rules", rules),
    "6": ("S3", s3),
    "7": ("Exit", exit_program),
}

# Main menu logic
def main_menu():
    while True:
        print("\n AWS Service Menu:")
        for key, (name, _) in services.items():
            print(f"{key}. {name}")

        choice = input("Enter your choice (1-7): ").strip()

        if choice in services:
            _, action = services[choice]
            action()
            again = input(" \n [*] Wanna Check (List) other Services ? (y/n) ").strip().lower()
            if again !="y":
                break
        else:
            print("❌ Invalid choice. Please try again.")

        time.sleep(1)

if __name__ == "__main__":
    main_menu()
