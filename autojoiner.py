try:
    import os
    import ssl
    import time
    import json
    import threading
    import random
    import ctypes
    import shutil
    import base64
    import cloudscraper
    import string
    import requests
    from termcolor import cprint
    from cloudscraper import create_scraper
    import asyncio
    import datetime
    from time import *
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from playwright.async_api import async_playwright
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    #from chromedriver_py import binary_path
    from webdriver_manager.chrome import ChromeDriverManager
    from websocket import WebSocketApp, WebSocketException
    import websocket
except ModuleNotFoundError as e:
    missing_module = str(e).split("'")[1]
    print(f"Installing {missing_module}...")
    os.system(f"pip install {missing_module}")
tokens = []
with open("config.json", "r+") as dataa:
    config = json.load(dataa)
    auth = config["authorization"]
    proxyc = config["proxies"]["proxies"]
    proxies = config["proxies"]["ip:port:user:pass"]
key = base64.b64encode(os.urandom(16))
keys = key.decode("utf-8")
# If your proxy requires authentication, include username and password
# Replace 'proxy_user' and 'proxy_pass' with your actual username and password
scraper = create_scraper()
# Rest of your imports and setup
def banner():
    cprint("  ___        _         ______      _           ___       _                 ".center(shutil.get_terminal_size().columns), "light_blue")
    cprint(" / _ \      | |        | ___ \    (_)         |_  |     (_)                ".center(shutil.get_terminal_size().columns), "light_blue")
    cprint("/ /_\ \_   _| |_ ___   | |_/ /__ _ _ _ __       | | ___  _ _ __   ___ _ __ ".center(shutil.get_terminal_size().columns), "light_blue")
    cprint("|  _  | | | | __/ _ \  |    // _` | | '_ \      | |/ _ \| | '_ \ / _ \ '__|".center(shutil.get_terminal_size().columns), "light_blue")
    cprint("| | | | |_| | || (_) | | |\ \ (_| | | | | | /\__/ / (_) | | | | |  __/ |   ".center(shutil.get_terminal_size().columns), "light_blue")
    cprint("\_| |_/\__,_|\__\___/  \_| \_\__,_|_|_| |_| \____/ \___/|_|_| |_|\___|_|   ".center(shutil.get_terminal_size().columns), "light_blue")
    print("")
    cprint("Bloxflip Auto Rain Joiner #BY AOD".center(shutil.get_terminal_size().columns), "light_blue")
    print("")

banner()
def formatted_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    return str(formatted_time)

def error(text, content=None):
    cprint(f"[-] {text}{' > ' + content if content else ''}", "light_red")

def information(text):
    content = formatted_time() + f" [~] {text}"
    cprint(content, "light_green")

def uiprint(content, text):
    content2 = formatted_time() + " [" + content + "]" + f" {text}"
    cprint(content2, "light_yellow")

def rain(text, content=None):
    textt = formatted_time() + f" [$] {text}{' > ' + content if content else ''}"
    cprint(textt, "light_green")

def joinedplayer(text):
    content = formatted_time() + f" [+] {text}"
    cprint(content, "light_yellow")
class logger:
    def __init__(self, prefix: str = "Pepe"):
        self.WHITE: str = "\u001b[37m"
        self.MAGENTA: str = "\033[38;5;97m"
        self.MAGENTAA: str = "\033[38;2;157;38;255m"
        self.RED: str = "\033[38;5;196m"
        self.GREEN: str = "\033[38;5;40m"
        self.YELLOW: str = "\033[38;5;220m"
        self.BLUE: str = "\033[38;5;21m"
        self.PINK: str = "\033[38;5;176m"
        self.CYAN: str = "\033[96m"
        self.prefix: str = f"{self.PINK}[{self.MAGENTA}{prefix}{self.PINK}]"

    def get_time(self) -> str:
        return datetime.datetime.now().strftime("%H:%M:%S")
    
    def message(self, level: str, message: str, start: int = None, end: int = None) -> str:
        time_now = f" {self.PINK}[{self.MAGENTA}{self.get_time()}{self.PINK}] {self.WHITE}|"
        timer = f" {self.MAGENTAA}In{self.WHITE} -> {self.MAGENTAA}{str(end - start)[:5]} Seconds" if start and end else ""
        return f"{self.prefix} {self.WHITE}|{time_now} {self.PINK}[{level}{self.PINK}] {self.WHITE}-> {self.PINK}[{self.MAGENTA}{message}{self.PINK}]{timer}"
    
    def success(self, message: str, start: int = None, end: int = None, level: str = "Success") -> None:
        print(self.message(f"{self.GREEN}{level}", f"{self.GREEN}{message}", start, end))

    def info(self, message: str, start: int = None, end: int = None, level: str = "Info") -> None:
        print(self.message(f"{self.BLUE}{level}", f"{self.BLUE}{message}", start, end))

    def failure(self, message: str, start: int = None, end: int = None, level: str = "Failure") -> None:
        print(self.message(f"{self.RED}{level}", f"{self.RED}{message}", start, end))
    
    def rain(self, message: str, start: int = None, end: int = None, level: str = "Rain") -> None:
        print(self.message(f"{self.CYAN}{level}", f"{self.CYAN}{message}", start, end))
    def input(self, message: str, level: str = "Input") -> None:
        time_now = f" {self.PINK}[{self.MAGENTA}{self.get_time()}{self.PINK}] {self.WHITE}|"
        input(f"{self.prefix} {self.WHITE}|{time_now} {self.YELLOW}[{level}{self.YELLOW}] {self.WHITE}-> {self.YELLOW}[{self.YELLOW}{message}{self.YELLOW}] -> {self.PINK}")

log = logger()
# s = time.time()
# logger.info(f"Successfully Got HSW {hsw[:80]} / Length: {len(hsw)} / Time: {str(time.time() - s)[:5]}", "Success")
def get_roblox_username(auth, proxy=None):
    # Initialize the proxy dictionary
    if proxyc:
        ip, port, user, passw = proxies.split(':')
        proxy_url = f"http://{user}:{passw}@{ip}:{port}"
        proxy = {
            "http": proxy_url,
            "https": proxy_url
        }

    # Create a scraper with the proxy settings
    scraper = cloudscraper.create_scraper()
    
    if proxyc:
        scraper.proxies.update(proxy)
    
    try:
        response = scraper.get("https://api.bloxflip.com/user", headers={"x-auth-token": auth})
        response.raise_for_status()  # Check for HTTP errors
        info = response.json().get('user', {})
        return info.get('robloxUsername', 'Unknown')
    except Exception as e:
        print(f"Failed to get Roblox username: {e}")
        return 'Error'
def change_title():
    start_time = time()
    roblox_username = get_roblox_username(auth)  # Fetch the username once
    url = f"https://api.github.com/repos/aodhub2329/Bloxflip-Auto-Joiner/commits?path=BloxFlip%20Auto%20Joiner.py&per_page=1"
    
    # Gá»­i yÃªu cáº§u GET Äáº¿n GitHub API
    response = requests.get(url)
    
    # Kiá»m tra náº¿u yÃªu cáº§u thÃ nh cÃ´ng (mÃ£ tráº¡ng thÃ¡i HTTP 200)
    if response.status_code == 200:
        # Láº¥y thÃ´ng tin vá» commit tá»« pháº£n há»i
        commit_info = response.json()
        
        # TrÃ­ch xuáº¥t cÃ¡c thÃ´ng tin quan trá»ng vá» commit
        if commit_info:
            commit = commit_info[0]
            commit_sha = commit['sha']
    while True:
        # Káº¿t há»£p thá»i gian vÃ  dÃ£y kÃ½ tá»± ngáº«u nhiÃªn vÃ o tiÃªu Äá»
        elapsed_time = int(time() - start_time)
        # TÃ­nh sá» giá», sá» phÃºt vÃ  sá» giÃ¢y
        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60

        title = f"{hours:02d}:{minutes:02d}:{seconds:02d} | {commit_sha} | Logged in as: {roblox_username} | v2.2"
        # In tiÃªu Äá» má»i ra console
        # Äáº·t tiÃªu Äá» má»i
        # (LÆ°u Ã½: chá»©c nÄng nÃ y chá» hoáº¡t Äá»ng trÃªn má»t sá» mÃ´i trÆ°á»ng, khÃ´ng pháº£i trÃªn táº¥t cáº£ cÃ¡c há» Äiá»u hÃ nh)
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        except:
            pass
        sleep(0.2)
title_thread = threading.Thread(target=change_title)
title_thread.start()
log.input("Press Enter To Continue")
async def solve_captcha():
    # Láº¥y ÄÆ°á»ng dáº«n tuyá»t Äá»i cá»§a file Äang cháº¡y
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    # Chuyá»n Äá»i dáº¥u gáº¡ch chÃ©o ÄÆ¡n thÃ nh dáº¥u gáº¡ch chÃ©o kÃ©p
    converted_path = current_directory.replace("\\", "\\\\")

    # Äáº£m báº£o ÄÆ°á»ng dáº«n káº¿t thÃºc báº±ng dáº¥u gáº¡ch chÃ©o kÃ©p
    if not converted_path.endswith("\\\\"):
        converted_path += "\\\\"
    # Path to your extension file (.crx, .zip, etc.)
    extension_path = converted_path + "assets\\Hcaptcha-Solver.crx"
    # Set up Chrome options
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    chrome_options = Options()
    chrome_options.add_extension(extension_path)
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--window-size=800,800")
    chrome_options.add_argument("--disable-3d-apis")
    chrome_options.add_argument('--ignore-gpu-blacklist')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")
    chrome_options.add_argument("--disable-renderer-backgrounding")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-notifications")
    # Set up the ChromeDriver service
    service = Service(ChromeDriverManager().install())

    # Launch the browser
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the target URL
        driver.get("https://hcaptcha.projecttac.com/?sitekey=2ce02d80-0c81-4b28-8af5-e4cdfc08bed9")

        # Wait until the hCaptcha is solved
        timeout = 100000  # 100 seconds
        end_time = time() + timeout / 1000.0
        while time() < end_time:
            try:
                element = driver.find_element(By.CSS_SELECTOR, '[data-hcaptcha-response]')
                response_value = element.get_attribute('data-hcaptcha-response')
                if response_value and response_value != '':
                    driver.quit()
                    break
                    return response_value
            except Exception as e:
                sleep(1)
        driver.quit()
        return None
    except Exception as e:
        print(f'Error in captcha solving: {e}')
        driver.quit()
        return None
async def connect_websocket():
        s = time()
        log.rain("Joining Rain")
        url = "wss://ws.bloxflip.com/socket.io/?EIO=3&transport=websocket"
        headers = {
            "Host": "ws.bloxflip.com",
            "Connection": "Upgrade",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Upgrade": "websocket",
            "Origin": "https://bloxflip.com",
            "Sec-WebSocket-Version": "13",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US",
            "Sec-WebSocket-Key": keys,
        }
        if proxyc:
            ip, port, login, password = proxies.split(':')
        ws = websocket.WebSocket()
        if proxyc:
            ws.connect(
                url,
                header=headers,
                http_proxy_host=ip,
                http_proxy_port=port,
                proxy_type="http",
                http_proxy_auth=(login, password)
            )
        else:
            ws.connect(
                url,
                header=headers
            )
        ws.send('40/chat,')
        queries1 = [
            "40/chat,",
            "40/cups,",
            "40/jackpot,",
            "40/rouletteV2,",
            "40/roulette,",
            "40/crash,",
            "40/wallet,",
            "40/marketplace,",
            "40/case-battles,",
            "40/mod-queue,",
            "40/feed,",
            "40/cloud-games,"
        ]

        TOKEN = auth
        t = [
            '42/chat,["auth", "' + TOKEN + '"]',
            '42/cups,["auth","' + TOKEN + '"]',
            '42/jackpot,["auth","' + TOKEN + '"]',
            '42/rouletteV2,["auth","' + TOKEN + '"]',
            '42/roulette,["auth","' + TOKEN + '"]',
            '42/crash,["auth","' + TOKEN + '"]',
            '42/wallet,["auth","' + TOKEN + '"]',
            '42/marketplace,["auth","' + TOKEN + '"]',
            '42/case-battles,["auth","' + TOKEN + '"]',
            '42/mod-queue,["auth","' + TOKEN + '"]',
            '42/cloud-games,["auth","' + TOKEN + '"]',
            '42/feed,["auth","' + TOKEN + '"]'
        ]
        for i in queries1:
            ws.send(i)
        for _ in t:
            ws.send(_)
        #loop = asyncio.new_event_loop()
        #asyncio.set_event_loop(loop)

        #token = loop.run_until_complete(solve_captcha())
        token = await solve_captcha()
        ws.send(f'42/chat,["enter-rain",{{"captchaToken":"{token};;undefined;;scope"}}]')
        sleep(3)
        info = cloudscraper.create_scraper().get("https://api.bloxflip.com/user", headers={"x-auth-token": auth}).json()['user']
        if proxyc:
            info = \
            cloudscraper.create_scraper().get("https://api.bloxflip.com/user", headers={"x-auth-token": TOKEN}, proxies={'http': f'http://{login}:{password}@{ip}:{port}'}).json()[
                'user']
        else:
            info = \
            cloudscraper.create_scraper().get("https://api.bloxflip.com/user", headers={"x-auth-token": TOKEN}).json()[
                'user']
        checker = cloudscraper.create_scraper().get("https://api.bloxflip.com/chat/history").json()['rain']['players']
        if info['robloxId'] in checker:
            log.rain(f"Account Joined: {info['robloxUsername']}, Current balance: {round(info['wallet'])}", s, time())
            ws.close()
        else:
            log.rain(f"Account Not Joined: {info['robloxUsername']}", s, time())
def keep_alive(ws):
    try:
        while True:
            sleep(30)
            ws.send("2")
    except Exception as e:
        pass
def on_message(ws, msg):
    if 'rain-state-changed' in msg:
        try:
            data = json.loads(msg.replace("42/chat,", ""))[1]
            if data.get("active"):
                if data["active"] == True and data['prize'] > 198:
                    log.rain(f"Rain Funded! / Robux: {data['prize']} / Host: {data['host']}")
                    threading.Thread(target=asyncio.run, args=(connect_websocket(),)).start()
            elif data == False:
                log.rain("Rain ended.")
        except Exception as e:
            pass
    elif "pingInterval" in msg:
        threading.Thread(target=keep_alive, args=(ws,)).start()
        ws.send("40/chat,")

def on_open(_):
    log.info("Connected!")
def on_err(_, err):
    log.failure(f"error: {err}")
headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US',
    'Cache-Control': 'no-cache',
    'Connection': 'Upgrade',
    'Pragma': 'no-cache',
    'Upgrade': 'websocket',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
scraper = create_scraper()
log.info("Wait For Checking Rain...")
while True:
    try:
        wsa = WebSocketApp("wss://ws.bloxflip.com/socket.io/?EIO=3&transport=websocket", header=headers,
                           on_open=on_open, on_message=on_message, on_error=on_err)
        wsa.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE}, origin="https://bloxflip.com", host="ws.bloxflip.com",
                        reconnect=True)
    except WebSocketException as e:
        print(f'here websocket except error {e}')
        sleep(5)
        continue



#AOD MADE THIS! 😘
