#edit ec2 - attch dettach ebs 
#all
import os
import boto3
import sys 
import time 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ServiceawsDM import fakeload


base_dir = os.path.dirname(os.path.abspath(__file__))
def ebsattach():
    fakeload("EBS Attach")
    Attachebs_script = os.path.join(base_dir, "Edit", "Attachebs.py")
    os.system(f"python3 {Attachebs_script}")

def ebsdetach():
    fakeload("EBS Detach")
    Detachebs_script = os.path.join(base_dir, "Edit", "Detachebs.py")
    os.system(f"python3 {Detachebs_script}")

def releaseip():
    fakeload("IP Release")
    IPelease_script = os.path.join(base_dir, "Edit", "Releaseip.py")
    os.system(f"python3 {IPelease_script}")

def attachipec2():
    fakeload("Ec2 Ip Attach")
    Attachipec2_script = os.path.join(base_dir, "Edit", "Attachipec2.py")
    os.system(f"python3 {Attachipec2_script}")

def Securitygrp():
    fakeload("Security Group Editing")
    secgrp_script = os.path.join(base_dir, "Edit", "Securitygrpedit.py")
    os.system(f"python3 {secgrp_script}")

def Hostwebec2():
    fakeload("Ec2 web Host")
    hostwebec2_script = os.path.join(base_dir, "Edit", "Hostwebec2.py")
    os.system(f"python3 {hostwebec2_script}")


Editservices ={
    "1" : ("Attach Ebs ", ebsattach),
    "2" : ("Detach Ebs ", ebsdetach),
    "3" : ("Release IP ", releaseip),
    "4" : ("IP Attach to Ec2", attachipec2),
    "5" : ("Security", Securitygrp),
    "6":("Website host by Ec2", Hostwebec2)
}

def main():
    while True:
        print ("AWS EDIT MENU :")
        for key ,(name ,i) in Editservices.items():
            print (f"{key}, {name}")
        
        choice=input ("Enter Your choice (1-5) :").strip()

        if choice in Editservices:
            i,action = Editservices[choice]
            action()
            again = input(" \n [*] Wanna Check (List) other Services ? (y/n) ").strip().lower()
            if again !="y":
                break
        else :
            print("❌ Invalid Choice ")

        time.sleep(1)



# def attachipec2():
#     fakeload("Ec2 Ip Attach")
#     Attachipec2_script = os.path.join(base_dir, "Edit", "Attachipec2.py")
#     os.system(f"python3 {Attachipec2_script}")

print ("uc")
if __name__ == "__main__":
    print ("                    +++ Edit Panel MCloud +++")
    main()

