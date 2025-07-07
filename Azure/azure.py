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
                       .                    MCloud - Azure         .
                       .                                           .
                       .  .  .  .  . .  .  .  .  .  .  .  .  .  .  . 
'''

def main():
    if platform.system() != "Windows":
        print("[!] This tool only supports Windows.")
        return
    print(BANNER)
    print("MCloud Service for Azure is Under Construction.......")
    print("see you soon")
    print("                          -Mojo824")
    time.sleep(2)

if __name__ == "__main__":
    main()
