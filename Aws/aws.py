import os
import sys
import subprocess
import time
import platform

BANNER = '''
                       .  .  .  .    .  .  .  .  .  .  .  .  .  .  . 
                       .                                           .
                       .   __  __  _____ _                 _       .
                       .  |  \/  |/ ____| |               | |      .
                       .  | \  / | |    | | ___  _   _  __| |      .
                       .  | |\/| | |    | |/ _ \| | | |/ _` |      .
                       .  | |  | | |____| | (_) | |_| | (_| |      .
                       .  |_|  |_|\_____|_|\___/ \__,_|\__,_|      .
                       .                                           .
                       .                    MCloud - AWS           .
                       .                                           .
                       .  .  .  .  . .  .  .  .  .  .  .  .  .  .  . 
'''

FLAG_FILE = ".MCloudaws_installed.flag"

def check_aws_cli():
    try:
        subprocess.check_output(["aws", "--version"], stderr=subprocess.STDOUT)
        print("AWS CLI found")
        return True
    except Exception:
        print("AWS CLI not found !!")
        res = input("Do you want to install AWS CLI? (Y/N): ")
        if res.lower() == 'y':
            print("Please download and install AWS CLI for Windows from:")
            print("https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html")
            input("Press Enter after installing AWS CLI to continue...")
            return check_aws_cli()
        else:
            print("Install AWS CLI manually. Exiting.......")
            sys.exit(1)

def check_boto3():
    try:
        import boto3
        print("[✓] boto3 is already installed.")
    except ImportError:
        print("[!] boto3 not found. Attempting installation...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "boto3"])
        print("[+] boto3 installed successfully.")

def aws_configure():
    print("Launching 'aws configure'...")
    os.system("aws configure")

def main():
    if platform.system() != "Windows":
        print("[!] This tool only supports Windows.")
        return
    print(BANNER)
    print("                 ==== MCloud AWS Service ====                ")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.isdir(base_dir):
        print("Base directory not found. Exiting...")
        sys.exit(1)
    print("Starting...")
    time.sleep(2)
    print("Configuring  AWS ...")
    time.sleep(2)
    if not os.path.exists(os.path.join(base_dir, FLAG_FILE)):
        print("[*] Welcome to 'MCLOUD Aws' for the first-time setup...")
        check_aws_cli()
        time.sleep(2)
        print("[*] Checking for boto3 module...")
        check_boto3()
        with open(os.path.join(base_dir, FLAG_FILE), 'w') as f:
            f.write('installed')
    aws_configure()
    print("What you wanna do \n 1.New Deploy \n 2.Edit or Make changes to any service \n 3.View you Services (List) \n 4.Dangerzone ")
    resD = input("Your Response: ")
    if resD == "1":
        os.system(f'python "{os.path.join(base_dir, "ServiceawsDM.py")}"')
    elif resD == "2":
        os.system(f'python "{os.path.join(base_dir, "Serviceawsedit.py")}"')
    elif resD == "3":
        os.system(f'python "{os.path.join(base_dir, "ServiceawsLM.py")}"')
    elif resD == "4":
        confirm = input("Are you confirm to enter DangerZone (only y to confirm press any key to cancel): ")
        if confirm.lower() == 'y':
            os.system(f'python "{os.path.join(base_dir, "DangerZone.py")}"')
        else:
            print("Exitingggg..")
            sys.exit(1)
    else:
        print("Invalid Input Please Re-run")
        sys.exit(1)
    time.sleep(2)
    print("Thanks for using this MCloud !")
    print("Happy Clouding f2 Aws")

if __name__ == "__main__":
    main()
