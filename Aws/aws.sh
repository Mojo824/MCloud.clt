#!/bin/bash

cat << "EOF"
                       .  .  .  .    .  .  .  .  .  .  .  .  .  .  . 
                       .                                           .
                       .   __  __  _____ _                 _       .
                       .  |  \/  |/ ____| |               | |      .
                       .  | \  / | |    | | ___  _   _  __| |      .
                       .  | |\/| | |    | |/ _ \| | | |/ _` |      .
                       .  | |  | | |____| | (_) | |_| | (_| |      .
                       .  |_|  |_|\_____|_|\___/ \__,_|\__,_|      .
                       .                                           .
                       .             MCloud - Aws                  .
                       .                                           .
                       .  .  .  .  . .  .  .  .  .  .  .  .  .  .  . 
EOF
echo "                 ==== MCloud AWS Service ====                "

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ ! -d "$BASE_DIR" ]; then
    echo "Base directory not found. Exiting..."
    exit 1
fi

echo "Starting..."
sleep 2
echo "Configuring  AWS ..."
sleep 2
if [ ".MCloudaws_installed.flag" ]; then 
    echo "Welcome Again "
fi

if [ ! -f ".MCloudaws_installed.flag" ]; then
    echo "[*] Welcome to "MCLOUD Aws" for the first-time setup..."
    if ! command -v aws >/dev/null 2>&1; then
        echo "AWS CLI not found !!"
        read -p "Do you want to install AWS CLI? (Y/N): " res

        if [[ "$res" == "y" || "$res" == "Y" ]]; then
            curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
            unzip awscliv2.zip
            sudo ./aws/install
        elif [[ "$res" == "n" || "$res" == "N" ]]; then 
            echo -e "Install AWS CLI manually.\nExiting......."
            exit 1
        else 
            echo -e "Invalid Input !!\nExiting....."
            exit 1
        fi
    else 
        echo "AWS CLI found"
    fi

    sleep 2
    echo "[*] Checking for boto3 module..."

    if ! python3 -c "import boto3" 2>/dev/null; then
        echo "[!] boto3 not found. Attempting installation..."
    
        if command -v pip3 >/dev/null 2>&1; then
            sudo pip3 install boto3 --break-system-packages 
        elif command -v pip >/dev/null 2>&1; then
            sudo pip install boto3
        else
            echo "[✗] pip is not installed. Please install pip to proceed Manually ."
            exit 1
        fi

        echo "[+] boto3 installed successfully."
    else
        echo "[✓] boto3 is already installed."
    fi
    sudo touch .MCloudaws_installed.flag
fi

aws configure

echo -e "What you wanna do \n 1.New Deploy \n 2.Edit or Make changes to any service \n 3.View you Services (List) \n 4.Dangerzone "
read -p "Your Response " resD

if [[ "$resD" == "1" ]]; then 
    python3 $BASE_DIR/ServiceawsDM.py
elif [[ "$resD" == "2" ]]; then 
    python3 $BASE_DIR/Serviceawsedit.py
elif [[ "$resD" == "3" ]]; then 
    python3 $BASE_DIR/ServiceawsLM.py
elif [[ "$resD" == "4" ]]; then 
    echo " Are you confirm to enter DangerZone (only y to confirm press any key to cancel ) "
    read -p " " confirm
    if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then 
        python3 $BASE_DIR/DangerZone.py
    else 
        echo "Exitingggg.."
        exit 1
    fi
else 
    echo "Invalid Input Please Re-run"
fi 

sleep 2
echo " Thanks for using this MCloud !"

echo "Happy Clouding f2 Aws"