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
                       .                    MCloud                 .
                       .                                           .
                       .  .  .  .  . .  .  .  .  .  .  .  .  .  .  . 
'''

def check_internet():
    try:
        subprocess.check_call(['ping', '-n', '1', 'google.com'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    if platform.system() != "Windows":
        print("[!] This tool only supports Windows.")
        ask=input("Do you want the linux version of this tool  ??\ny/n  :").strip().lower()
        if ask.lower() == 'y':
            os.system('start "https://github.com/Mojo824/MCloud.clt"')
        sys.exit(1)

    print(BANNER)
    if not check_internet():
        print("Internet Connection Not Found ")
        print("please Check internet connection ")
        sys.exit(1)
    while True:
        while True:
            print("Choose your Cloud \n1. Azure \n2. Aws ")
            res = input("your input (by num)  : ")
            if res == "1":
                os.system(f"python {os.path.join(os.path.dirname(__file__), 'Azure', 'azure.py')}")
                break
            elif res == "2":
                os.system(f"python {os.path.join(os.path.dirname(__file__), 'Aws', 'aws.py')}")
                break
            else:
                print("Invalid Input \n [*] Try Again !! ")
        confirm = input("Do you want to Run again ??\ny/n  :")
        if confirm.lower() != 'y':
            break
    flag_file = os.path.join(os.path.dirname(__file__), ".gitHub_Star.flag")
    if not os.path.exists(flag_file):
        time.sleep(2)
        print("Would you like to give it a ⭐ on GitHub?")
        time.sleep(2)
        choice = input("Type 'y' to confirm: ")
        if choice.lower() == 'y':
            print("🎉 You're awesome! Opening GitHub...")
            os.system('start "https://github.com/Mojo824/MCloud.clt"')
            print("Please give a star when it opens! ⭐")
            with open(flag_file, 'w') as f:
                f.write('starred')
        else:
            print("No worries! Have a great day 😊")
    print("Happy Clouding f1 ALLover")

if __name__ == "__main__":
    main()
