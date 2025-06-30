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
echo "Starting..."
sleep 2
echo "Configuring  AWS ..."
sleep 2
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

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if ! python3 -c "import boto3" 2>/dev/null; then
    echo "[!] boto3 not found. Attempting installation..."
    
    if command -v pip3 >/dev/null 2>&1; then
        sudo pip3 install boto3
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
sleep 2
echo "Would you like to give it a ⭐ on GitHub?"
sleep 2
read -p "Type 'y' to confirm: " choice

if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
    echo "🎉 You're awesome! Opening GitHub..."
    xdg-open "https://github.com/Mojo824/" 
    echo "Please give a star when it opens! ⭐"
else
    echo "No worries! Have a great day 😊"
fi
echo "Happy Clouding f2 Aws"