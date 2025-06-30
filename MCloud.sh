
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

echo -e "Choose your Cloud \n1. Azure \n2. Aws "
read -p "your input (by num)  : " res 

if [[ "$res" == "1" ]]; then
    bash $BASE_DIR/Azure/azure.sh
elif [[ "$res" == "2" ]]; then
    bash $BASE_DIR/Aws/aws.sh
else 
    echo "Invalid Input \n Exitingg.........."
    exit 1
fi   
echo "Happy Clouding f1 ALLover"

