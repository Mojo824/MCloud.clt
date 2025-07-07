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

        else 
            echo -e "Invalid Input \n [*] Try Again !! "
        fi  
    done      
    echo "Do you want to Run again ??"
    read -p "y/n  :" confirm
    if [[ "$confirm" != "y" || "$confirm" != "Y" ]] ; then 
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
        touch .gitHub_Star.flag  

    else
        echo "No worries! Have a great day 😊"
    fi
fi
echo "Happy Clouding f1 ALLover"


