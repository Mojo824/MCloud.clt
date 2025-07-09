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
                       .                    MCloud                 .
                       .                                           .
                       .  .  .  .  . .  .  .  .  .  .  .  .  .  .  . 
EOF

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! ping -c 4 google.com > /dev/null 2>&1; then
    echo "Internet Connection Not Found "
    echo "please Check internet connection "
    exit 1
fi 


# Add MCloud to /usr/local/bin if not already present or outdated
BIN_PATH="/usr/local/bin/MCloud"
BIN_BASE="/usr/local/bin"
OTHER_FOLDERS=("$BASE_DIR/Aws" "$BASE_DIR/Azure")
SCRIPT_PATH="$BASE_DIR/MCloud.sh"
if [ ! -f "$BIN_PATH" ] ; then
    echo "Welcome to MCloud For the first time "
    echo "First Time ?? (requires sudo)..."
    sudo cp -r "$SCRIPT_PATH" "$BIN_PATH"
    for folder in "${OTHER_FOLDERS[@]}"; do
        sudo cp -r "$folder" "$BIN_BASE"
    done
    sudo chmod +x "$BIN_PATH"
    echo "You can now run MCloud from anywhere using: MCloud"
else
    echo "Welcome To MCloud"
fi

#### please help if you are here #####


# # Check for updates for the whole project (in github)
# REPO_GIT_URL="https://github.com/Mojo824/MCloud.clt.git"
# if [ -d "$BASE_DIR/.git" ]; then
#     LOCAL_HASH=$(git -C "$BASE_DIR" rev-parse HEAD 2>/dev/null)
#     REMOTE_HASH=$(git ls-remote "$REPO_GIT_URL" HEAD | awk '{print $1}')
#     if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
#         echo "A new version of the MCloud project is available on GitHub."
#         read -p "Do you want to update the whole project now? (y/n): " update_all
#         if [[ "$update_all" == "y" || "$update_all" == "Y" ]]; then
#             sudo git -C "$BASE_DIR" pull
#             echo "Project updated to the latest version. Please restart the script."
#             exit 0
#         else
#             echo "Project update skipped."
#         fi
#     fi
# fi

while [ 1 ]; do  
    while [ 1 ]; do
        echo -e "Choose your Cloud \n1. Azure \n2. Aws "
        read -p "your input (by num)  : " res 
        if [[ "$res" == "1" ]]; then
            bash $BASE_DIR/Azure/azure.sh
            break 
        elif [[ "$res" == "2" ]]; then
            bash $BASE_DIR/Aws/aws.sh
            break
            sleep 1

        else 
            echo -e "Invalid Input \n [*] Try Again !! "
        fi  
        sleep 1
    done      
    echo "Do you want to Run again ??"
    read -p "y/n  :" confirm
    if [[ "$confirm" != "y" && "$confirm" != "Y" ]] ; then 
        break
    fi 
done 



if [ ! -f ".gitHub_Star.flag" ]; then

    sleep 2
    echo "Would you like to give it a ⭐ on GitHub?"
    sleep 2
    read -p "Type 'y' to confirm: " choice
    if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
        echo "🎉 You're awesome! Opening GitHub..."
        xdg-open "https://github.com/Mojo824/MCloud.clt" 
        echo "Please give a star when it opens! ⭐"
        sudo touch .gitHub_Star.flag  

    else
        echo "No worries! Have a great day 😊"
    fi
fi
echo "Happy Clouding f1 ALLover"


