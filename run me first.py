import os
try:
    from pystyle import Center, Colors, Colorate
    import subprocess
    import sys
except ModuleNotFoundError as e:
    missing_module = str(e).split("'")[1]
    print(f"Installing {missing_module}...")
    os.system(f"pip install {missing_module}")
os.system('cls' if os.name == 'nt' else 'clear')
os.system("title Download.net")

text = '''
______                          _                    _                  _   
|  _  \                        | |                  | |                | |  
| | | |  ___  __      __ _ __  | |  ___    __ _   __| |    _ __    ___ | |_ 
| | | | / _ \ \ \ /\ / /| '_ \ | | / _ \  / _ | / ` |   | ' \  /  | __|
| |/ / | () | \ V  V / | | |   () || (|  (| |  | | |   /| | 
|/   _/   _/_/  || |||_| _/  _,| _,|()|| || ___| _|


'''

print(Colorate.Diagonal(Colors.redtopurple, Center.XCenter(text)))

def installmodule(modulename):
    try:
        # Kiểm tra xem module đã được cài đặt chưa
        subprocess.check_output([sys.executable, '-m', 'pip', 'show', module_name])
    except subprocess.CalledProcessError as e:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name])

if __name == "__main":
    # Danh sách các module cần kiểm tra và cài đặt
    required_modules = [
        'termcolor',
        'cloudscraper',
        'requests',
        'selenium',
        'playwright',
        'webdriver_manager',
        'websocket-client',
        'websocket'
    ]

    # Kiểm tra và cài đặt các module cần thiết
    for module in required_modules:
        install_module(module)

input("downloaded successfully")`


#All rights goes to AOD
