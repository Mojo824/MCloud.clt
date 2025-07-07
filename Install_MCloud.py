import os
import sys
import shutil
import platform

INSTALL_PATH_WINDOWS = os.path.expandvars(r"%SystemRoot%\\System32\\MCloud.bat")

BANNER = """
MCloud Installer
================
"""

def is_admin():
    if os.name == 'nt':
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        return False  # Only support Windows

def install_windows():
    src = os.path.abspath("MCloud.py")
    bat_content = f"@echo off\npython \"{src}\" %*"
    with open(INSTALL_PATH_WINDOWS, 'w') as f:
        f.write(bat_content)
    print(f"Installed MCloud to {INSTALL_PATH_WINDOWS}")
    print("You can now run 'MCloud' from anywhere in cmd.")

def main():
    print(BANNER)
    if platform.system() != "Windows":
        print("[!] This installer only supports Windows.")
        sys.exit(1)
    if not is_admin():
        print("[!] Please run this installer as administrator.")
        sys.exit(1)
    install_windows()

if __name__ == "__main__":
    main()
