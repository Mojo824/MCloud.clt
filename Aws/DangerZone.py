import subprocess
import os

service_scripts = {
    'ebs': 'Deleteebs.py',
    'ec2': 'Deleteec2.py',
    'lambda': 'Deletelambda.py',
    'security group': 'Deletesecuritygrp.py',
    'subnet': 'Deletesubnet.py',
    'vpc': 'Deletevpc.py',
    'key pairs':'Deletekeypairs.py',
    's3':'Deletes3.py'
}

aws_dir = os.path.dirname(os.path.abspath(__file__))
dz_dir = os.path.join(aws_dir, 'Danger zone')

print("DANGER ZONE: Resource Deletion")

while True:
    print("\nWhich AWS service resource do you want to delete?")
    for idx, key in enumerate(service_scripts.keys(), 1):
        print(f"{idx}. {key.title()}")
    choice = input("Enter the number of the service (or 'q' to quit): ").strip()
    if choice.lower() == 'q':
        print("Exiting Danger Zone.")
        break
    try:
        idx = int(choice)
        if 1 <= idx <= len(service_scripts):
            service = list(service_scripts.keys())[idx-1]
            confirm = input(f"Are you sure you want to delete {service.upper()} resources? (yes/no): ").strip().lower()
            if confirm == 'yes':
                script_path = os.path.join(dz_dir, service_scripts[service])
                subprocess.run(['python3', script_path])
            else:
                print("Operation cancelled.")
        else:
            print("Invalid selection. Please try again.")
    except Exception:
        print("Invalid input. Please enter a valid number or 'q' to quit.")
