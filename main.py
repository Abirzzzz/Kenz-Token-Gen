import asyncio
import random
import string
import os
import sys 
import json
import httpx
import requests
import zendriver as zd
import pyautogui as ca
import pyperclip
import imaplib
import email
import re
import hashlib
from datetime import datetime
from colorama import Fore, Style, init
from pystyle import Colorate, Colors, Center
import io
import time
import uuid
import concurrent.futures
from base64 import b64encode
from json import dumps, loads, JSONDecodeError
from pathlib import Path
from platform import system, release, version
from random import choice
from typing import Optional, List, Tuple, Any, Dict, Union
from PIL import Image
import tls_client
import websocket

init(autoreset=True)

OUTPUT_DIR = "input"
ONLY_TOKEN_FILE = f"{OUTPUT_DIR}/tokens.txt"
FULL_DATA_FILE = f"{OUTPUT_DIR}/token.txt"
os.makedirs(OUTPUT_DIR, exist_ok=True)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
]

UA_POOL = []

def refresh_ua_pool():
    global UA_POOL
    UA_POOL = USER_AGENTS.copy()
    random.shuffle(UA_POOL)

class Neon:
    PURPLE_DARK = "\033[38;2;128;0;255m"
    PURPLE_MED = "\033[38;2;147;51;255m"
    PURPLE_LIGHT = "\033[38;2;166;102;255m"
    MAGENTA_DARK = "\033[38;2;255;0;255m"
    MAGENTA_MED = "\033[38;2;255;51;255m"
    MAGENTA_LIGHT = "\033[38;2;255;102;255m"
    PINK = "\033[95m"
    PURPLE = "\033[95m"
    MAGENTA = "\033[35m"
    LIGHT_MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    END = "\033[0m"
    
    
    GRADIENT_PURPLE = [
        "\033[38;2;128;0;255m",   # Dark Purple
        "\033[38;2;147;51;255m",   # Purple
        "\033[38;2;166;102;255m",  # Light Purple
        "\033[38;2;185;153;255m",  # Lavender
        "\033[38;2;204;204;255m",  # Very Light Purple
    ]
    
    GRADIENT_MAGENTA = [
        "\033[38;2;255;0;255m",    # Magenta
        "\033[38;2;255;51;255m",   # Light Magenta
        "\033[38;2;255;102;255m",  # Pink
        "\033[38;2;255;153;255m",  # Light Pink
        "\033[38;2;255;204;255m",  # Very Light Pink
    ]

def gradient_text(text, colors=None):
    if colors is None:
        colors = Neon.GRADIENT_MAGENTA
    result = ""
    for i, char in enumerate(text):
        color_index = i % len(colors)
        result += f"{colors[color_index]}{char}"
    return result + Neon.END

def show_neon_art():
    """Display animated neon ASCII art that pulses for 5 seconds"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    art = r"""
                               /T /I
                              / |/ | .-~/
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l  |  T  /
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]
^.___~"--._    ~-{  .-~ .  `\ Y . /    |
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.
              (_/ .  ~(   /'     "~"--,Y   -=b-. _)
               (_/ .  \  :           / l      c"~o \
                \ /    `.    .     .^   \_.-~"~--.  )
                 (_/ .   `  /     /       !       )/
                  / / _.   '.   .':      /        '
                  ~(_/ .   /    _  `  .-<_      
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K   "-.~-.______//
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                      /' /\     \  \     ,v=.  ((
                    .^. / /\     "  }__ //===-  `
                   / / ' '  "-.,__ {---(==-
                 .^ '       :  T  ~"   ll
                / .  .  . : | :!        \\
               (_/  /   | | j-"          ~^
                 ~-<_(_.^-~"
"""
    
    
    start_time = time.time()
    pulse_count = 0
    
    while time.time() - start_time < 5:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        if pulse_count % 2 == 0:
            
            colored_art = ""
            for line in art.split('\n'):
                colored_art += gradient_text(line, Neon.GRADIENT_MAGENTA) + "\n"
            print(colored_art)
        else:
            
            colored_art = ""
            for line in art.split('\n'):
                colored_art += gradient_text(line, Neon.GRADIENT_PURPLE) + "\n"
            print(colored_art)
        
        
        subtitle = "KenzShop x Aliucord"
        print(f"\n{gradient_text(subtitle.center(60), Neon.GRADIENT_MAGENTA)}")
        
        
        time.sleep(0.5)
        pulse_count += 1
    
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    colored_art = ""
    for line in art.split('\n'):
        colored_art += gradient_text(line, Neon.GRADIENT_MAGENTA) + "\n"
    print(colored_art)
    print(f"\n{gradient_text('KenzShop x Aliucord'.center(60), Neon.GRADIENT_MAGENTA)}")
    time.sleep(0.5)

def print_banner(banner_type="main"):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if banner_type == "main":
        banner = f"""
{Neon.MAGENTA}{Neon.BOLD} ██ ▄█▀▓█████  ███▄    █ ▒███████▒
 ██▄█▒ ▓█   ▀  ██ ▀█   █ ▒ ▒ ▒ ▄▀░
▓███▄░ ▒███   ▓██  ▀█ ██▒░ ▒ ▄▀▒░ 
▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒  ▄▀▒   ░
▒██▒ █▄░▒████▒▒██░   ▓██░▒███████▒
▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒
░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░░░▒ ▒ ░ ▒
░ ░░ ░    ░      ░   ░ ░ ░ ░ ░ ░ ░
░  ░      ░  ░         ░   ░ ░    
                         ░        {Neon.END}
"""
        print(banner)
        
    elif banner_type == "generator":
        banner = f"""
{Neon.MAGENTA}{Neon.BOLD}▄▄▄▄▄      ▄ •▄ ▄▄▄ . ▐ ▄      ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
•██  ▪     █▌▄▌▪▀▄.▀·•█▌▐█    ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
 ▐█.▪ ▄█▀▄ ▐▀▀▄·▐▀▀▪▄▐█▐▐▌    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
 ▐█▌·▐█▌.▐▌▐█.█▌▐█▄▄▌██▐█▌    ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
 ▀▀▀  ▀█▄▀▪·▀  ▀ ▀▀▀ ▀▀ █▪    ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀ {Neon.END}
"""
        print(banner)
        
    elif banner_type == "humanizer":
        banner = f"""
{Neon.MAGENTA}{Neon.BOLD}▄▄▄▄▄      ▄ •▄ ▄▄▄ . ▐ ▄      ▄ .▄▄• ▄▌• ▌ ▄ ·.  ▄▄▄·  ▐ ▄ ▪  ·▄▄▄▄•▄▄▄ .▄▄▄  
•██  ▪     █▌▄▌▪▀▄.▀·•█▌▐█    ██▪▐██▪██▌·██ ▐███▪▐█ ▀█ •█▌▐███ ▪▀·.█▌▀▄.▀·▀▄ █·
 ▐█.▪ ▄█▀▄ ▐▀▀▄·▐▀▀▪▄▐█▐▐▌    ██▀▐██▌▐█▌▐█ ▌▐▌▐█·▄█▀▀█ ▐█▐▐▌▐█·▄█▀▀▀•▐▀▀▪▄▐▀▀▄ 
 ▐█▌·▐█▌.▐▌▐█.█▌▐█▄▄▌██▐█▌    ██▌▐▀▐█▄█▌██ ██▌▐█▌▐█ ▪▐▌██▐█▌▐█▌█▌▪▄█▀▐█▄▄▌▐█•█▌
 ▀▀▀  ▀█▄▀▪·▀  ▀ ▀▀▀ ▀▀ █▪    ▀▀▀ · ▀▀▀ ▀▀  █▪▀▀▀ ▀  ▀ ▀▀ █▪▀▀▀·▀▀▀ • ▀▀▀ .▀  ▀{Neon.END}
"""
        print(banner)
    credit_text = "made by Kenz x Aliucord"
    print(f"\n{gradient_text(credit_text, Neon.GRADIENT_MAGENTA)}")
    print(f"{gradient_text('═' * 60, Neon.GRADIENT_PURPLE)}\n")
    print(f"{gradient_text('═' * 60, Neon.GRADIENT_PURPLE)}\n")

class EmailManager:
    def __init__(self):
        self.email = None
        self.mail_token = None
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0",
            "Accept": "application/json",
        })
        self.used_email_ids = set()

    async def generate_email(self):
        """Generate email from tempmail.lol"""
        max_attempts = 5
        
        for attempt in range(1, max_attempts + 1):
            try:
                
                
                r = self.session.get("https://api.tempmail.lol/generate", timeout=10)
                
                if r.status_code == 200:
                    data = r.json()
                    email = data.get("address", "")
                    token = data.get("token", "")
                    
                    if email and token:
                        self.email = email
                        self.mail_token = token
                        print(f"{gradient_text(f'✓ Email Generated: {self.email}', Neon.GRADIENT_MAGENTA)}")
                        return self.email
                        
            except Exception as e:
                print(f"{gradient_text(f'! Email API error: {e}', Neon.GRADIENT_PURPLE)}")
            
            await asyncio.sleep(1)
        
        print(f"{gradient_text('✗ Failed to generate email after 5 attempts!', Neon.GRADIENT_PURPLE)}")
        return None

    async def get_verification_link(self):
        """Get verification link from tempmail.lol - wait up to 2 minutes"""
        if not self.mail_token:
            return None
        
        max_attempts = 40
        start_time = time.time()
        
        print(f"{gradient_text('! Waiting for verification email... (max 2 minutes)', Neon.GRADIENT_MAGENTA)}")
        
        for attempt in range(1, max_attempts + 1):
            try:
                r = self.session.get(f"https://api.tempmail.lol/v2/inbox?token={self.mail_token}", timeout=12)
                
                if r.status_code == 200:
                    mails = r.json().get("emails", [])
                    
                    for mail in mails:
                        mail_id = mail.get("_id")
                        if mail_id in self.used_email_ids:
                            continue
                        
                        subject = mail.get("subject", "")
                        body = mail.get("body", "") + mail.get("html", "")
                        
                        if "Discord" in subject and ("verify" in subject.lower() or "confirm" in subject.lower()):
                            patterns = [
                                r'https://click\.discord\.com/ls/click\?[^\s"\')]+',
                                r'https://click\.discord\.com/ls/click\?[^\s"]+',
                                r'https://[^\s"\']*discord[^\s"\']*verify[^\s"\']*',
                                r'https://discord\.com/verify#[^\s"\']+',
                                r'https://verify\.discord\.com/[^\s"\']+',
                                r'https://discord\.com/verify\?[^\s"\']+'
                            ]
                            
                            for pattern in patterns:
                                match = re.search(pattern, body)
                                if match:
                                    link = match.group(0)
                                    link = link.split('"')[0].split("'")[0].split(')')[0]
                                    self.used_email_ids.add(mail_id)
                                    
                                    elapsed = int(time.time() - start_time)
                                    print(f"{gradient_text(f'✓ Verification link received! ({elapsed} seconds)', Neon.GRADIENT_MAGENTA)}")
                                    return link
                
                if attempt % 10 == 0:
                    elapsed = int(time.time() - start_time)
                    remaining = 120 - elapsed
                    if remaining > 0:
                        print(f"{gradient_text(f'! Still waiting for verification email... ({elapsed}s / 120s)', Neon.GRADIENT_MAGENTA)}")
                
            except Exception as e:
                print(f"{gradient_text(f'! Inbox check error: {e}', Neon.GRADIENT_PURPLE)}")
            
            await asyncio.sleep(3)
        
        print(f"{gradient_text('✗ No verification email found after 2 minutes!', Neon.GRADIENT_PURPLE)}")
        return None

class DiscordBot:
    def __init__(self, index, ua=None):
        self.index = index
        self.email_mgr = EmailManager()
        self.browser = None
        self.email = ""
        self.password = self._generate_pass()
        self.ua = ua
        self.verification_warning_shown = False

    def _generate_pass(self):
        words = ["Nxght", "V0id", "Cyb3r", "G1itch", "Sy5tem", "0perat0r", "Kenz", "Aliucord"]
        return f"{random.choice(words)}!{random.randint(1000, 9999)}"

    async def extract_token(self, page):
        script = """
        (function() {
            try {
                let m;
                window.webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]);
                let token = m.find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken();
                if (token) return token;
            } catch (e) {}
            try {
                let token = document.body.appendChild(document.createElement('iframe')).contentWindow.localStorage.token;
                if (token) return token.replace(/"/g, "");
            } catch (e) {}
            return null;
        })();
        """
        try:
            return await page.evaluate(script)
        except:
            return None

    async def check_is_verified(self, token):
        try:
            async with httpx.AsyncClient() as client:
                res = await client.get(
                    "https://discord.com/api/v9/users/@me",
                    headers={"Authorization": token}
                )
                if res.status_code == 200:
                    data = res.json()
                    return data.get("verified", False)
        except:
            pass
        return False

    async def wait_for_verification(self, page):
        print(f"{gradient_text('! Waiting for verify email', Neon.GRADIENT_MAGENTA)}")
        verification_shown = False
        
        while True:
            token = await self.extract_token(page)
            if token and len(str(token)) > 30:
                is_verified = await self.check_is_verified(token)
                if is_verified:
                    return token
                else:
                    if not verification_shown:
                        print(f"{gradient_text('✓ Token found, waiting for verification...', Neon.GRADIENT_PURPLE)}")
                        verification_shown = True
            await asyncio.sleep(5)

    async def start(self):
        self.email = await self.email_mgr.generate_email()
        if not self.email:
            print(f"{gradient_text(f'✗ Failed to generate email for Account #{self.index}', Neon.GRADIENT_PURPLE)}")
            return
        
        print(f"{gradient_text(f'▶ Opening Browser for Account #{self.index}', Neon.GRADIENT_MAGENTA)}")
        
        try:
            selected_ua = self.ua if self.ua else random.choice(USER_AGENTS)
            browser_args = [
                "--no-sandbox", 
                "--disable-blink-features=AutomationControlled",
                "--window-size=1280,720",
                "--disable-infobars",
                "--disable-notifications",
                "--disable-save-password-bubble",
                "--guest",
                f"--user-agent={selected_ua}"
            ]

            self.browser = await zd.start(arguments=browser_args)
            page = await self.browser.get("https://discord.com/register")
            await page.wait_for('input[name="email"]', timeout=60)
            
            y2k_names = ["kenzshopgen", "Aliucordgen", "kenzcustomer", "AliucordCustomer", "ilovekenz", "iloveAliucord", "kenzgen", "kenz", "aliucord", "etipuf", "whynot", "root", "user", "windows"]
            suffix_numbers = ''.join(random.choices(string.digits, k=random.randint(3, 5)))
            styles = [f"{random.choice(y2k_names)}_{suffix_numbers}", f"xX_{random.choice(y2k_names)}_{suffix_numbers}_Xx", f"{random.choice(y2k_names)}.{suffix_numbers}"]
            username = random.choice(styles)

            await asyncio.sleep(random.uniform(1.5, 3.0))

            inject_script = f"""
            (() => {{
                const setValue = (selector, value) => {{
                    const el = document.querySelector(selector);
                    if (el) {{
                        const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                        setter.call(el, value);
                        el.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    }}
                }};
                setValue('input[name="email"]', '{self.email}');
                setValue('input[name="username"]', '{username}');
                setValue('input[name="password"]', '{self.password}');
            }})();
            """
            await page.evaluate(inject_script)
            await asyncio.sleep(random.uniform(0.5, 1.2))

            for _ in range(4): 
                ca.press('tab')
                await asyncio.sleep(random.uniform(0, 0))
            
            used_months = random.sample(range(1, 13), 12)
            used_days = random.sample(range(1, 29), 28)
            
            ca.press('enter')
            await asyncio.sleep(random.uniform(0.4, 0.7))
            for _ in range(used_months[random.randint(0, 11)]): 
                ca.press('down')
                await asyncio.sleep(random.uniform(0.02, 0.05))
            ca.press('enter')
            
            await asyncio.sleep(random.uniform(0.3, 0.5))
            ca.press('tab')
            ca.press('enter')
            for _ in range(used_days[random.randint(0, 27)]): 
                ca.press('down')
                await asyncio.sleep(random.uniform(0.02, 0.05))
            ca.press('enter')
            
            await asyncio.sleep(random.uniform(0.3, 0.5))
            ca.press('tab')
            ca.press('enter')
            for _ in range(random.randint(20, 40)): 
                ca.press('down')
                await asyncio.sleep(random.uniform(0.01, 0.03))
            ca.press('enter')
            
            await asyncio.sleep(random.uniform(0, 0))
            for _ in range(4): 
                ca.press('tab')
                await asyncio.sleep(random.uniform(0, 0))
            ca.press('enter')

            print(f"{gradient_text('! Waiting for verification email...', Neon.GRADIENT_MAGENTA)}")
            verification_link = await self.email_mgr.get_verification_link()
            
            if verification_link:
                print(f"{gradient_text('✓ Verification link found! Opening...', Neon.GRADIENT_MAGENTA)}")
                await page.goto(verification_link)
                await asyncio.sleep(5)
            else:
                print(f"{gradient_text('! No verification link found, trying to get token anyway...', Neon.GRADIENT_MAGENTA)}")

            token = await self.wait_for_verification(page)
            
            if token:
                with open(ONLY_TOKEN_FILE, "a") as f1:
                    f1.write(f"{token}\n")
                with open(FULL_DATA_FILE, "a") as f2:
                    f2.write(f"{self.email}:{self.password}:{token}\n")
                print(f"{gradient_text(f'✓ Account #{self.index} verified successfully!', Neon.GRADIENT_MAGENTA)}")
            else:
                print(f"{gradient_text(f'✗ Account #{self.index} failed!', Neon.GRADIENT_PURPLE)}")
            
            await self.browser.stop()
        except Exception as e:
            print(f"{gradient_text(f'✗ Error: {e}', Neon.GRADIENT_PURPLE)}")
            if self.browser: 
                await self.browser.stop()


class HeaderGenerator:
    def __init__(self) -> None:
        self.base_chrome_version: int = 120
        self.impersonate_target: str = f"chrome_{self.base_chrome_version}"
        self.session: tls_client.Session = tls_client.Session(client_identifier=self.impersonate_target)
        self.ua_details: Dict[str, Any] = self._generate_ua_details()
        self._header_cache: Dict[Any, Dict[str, Any]] = {}
        self._cookie_cache: Dict[str, Dict[str, Any]] = {}

    def _generate_ua_details(self) -> Dict[str, Any]:
        chrome_major: int = self.base_chrome_version
        full_version: str = f"{chrome_major}.0.0.0"
        os_spec: str = self._get_os_string()
        platform_ua: str = f"Windows NT {release()}; Win64; x64" if "Windows" in os_spec else os_spec
        return {
            "user_agent": f"Mozilla/5.0 ({platform_ua}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{full_version} Safari/537.36",
            "chrome_version": full_version,
            "sec_ch_ua": [f'"Google Chrome";v="{chrome_major}"', f'"Chromium";v="{chrome_major}"', '"Not/A)Brand";v="99"']
        }

    def _get_os_string(self) -> str:
        os_map: Dict[str, str] = {"Windows": f"Windows NT 10.0; Win64; x64", "Linux": "X11; Linux x86_64", "Darwin": "Macintosh; Intel Mac OS X 10_15_7"}
        os_str: str = os_map.get(system(), "Windows NT 10.0; Win64; x64")
        if system() == "Windows":
            win_ver: list[str] = version().split('.')
            if len(win_ver) >= 2:
                os_str = f"Windows NT {win_ver[0]}.{win_ver[1]}; Win64; x64"
        return os_str

    def fetch_cookies(self, token: str) -> str:
        now: float = time.time()
        cache_entry: Optional[Dict[str, Any]] = self._cookie_cache.get(token)
        if cache_entry and now - cache_entry["timestamp"] < 86400:
            return cache_entry["cookie"]
        try:
            resp = self.session.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token})
            cookies: list[str] = []
            if "set-cookie" in resp.headers:
                set_cookie: Union[str, list[str]] = resp.headers["set-cookie"]
                if isinstance(set_cookie, list):
                    set_cookie = ", ".join(set_cookie)
                for cookie in set_cookie.split(", "):
                    cookie_part = cookie.split(";")[0]
                    if "=" in cookie_part:
                        name, value = cookie_part.split("=", 1)
                        cookies.append(f"{name}={value}")
            cookie_str: str = "; ".join(cookies)
            self._cookie_cache[token] = {"cookie": cookie_str, "timestamp": now}
            return cookie_str
        except:
            return ""

    def generate_super_properties(self) -> str:
        sp: Dict[str, Any] = {
            "os": system(), "browser": "Chrome", "device": "", "system_locale": "en-US",
            "browser_user_agent": self.ua_details["user_agent"], "browser_version": self.ua_details["chrome_version"].split(".0.")[0] + ".0.0.0",
            "os_version": str(release()), "referrer": "https://discord.com/", "referring_domain": "discord.com",
            "search_engine": "google", "release_channel": "stable", "client_build_number": 438971,
            "client_event_source": None, "has_client_mods": False, "client_launch_id": str(uuid.uuid4()),
            "launch_signature": str(uuid.uuid4()), "client_heartbeat_session_id": str(uuid.uuid4()), "client_app_state": "focused"
        }
        return b64encode(dumps(sp, separators=(',', ':')).encode()).decode()

    def generate_headers(self, token: str, location: Optional[str] = None, **kwargs) -> Dict[str, str]:
        base_headers: Dict[str, str] = {
            'accept': '*/*', 'accept-encoding': 'gzip, deflate, br, zstd', 'Accept-Language': 'en;q=1.0',
            'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i',
            "sec-ch-ua": ", ".join(self.ua_details["sec_ch_ua"]), "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": '"Windows"',
            'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
            "user-agent": self.ua_details["user_agent"], "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US", "x-discord-timezone": "America/Los_Angeles",
            "x-super-properties": self.generate_super_properties()
        }
        headers = base_headers.copy()
        headers["Authorization"] = token
        headers["cookie"] = self.fetch_cookies(token)
        return headers

def get_session_id(token: str) -> Optional[str]:
    ws: websocket.WebSocket = websocket.WebSocket()
    try:
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        hello: dict = loads(ws.recv())
        payload: dict = {"op": 2, "d": {"token": token, "properties": {"$os": "Windows", "$browser": "Chrome", "$device": "PC"}, "presence": {"status": "online", "since": 0, "activities": [], "afk": False}}}
        ws.send(dumps(payload))
        timeout = time.time() + 10
        while time.time() < timeout:
            response: dict = loads(ws.recv())
            if response.get("t") == "READY":
                session_id = response["d"]["session_id"]
                ws.close()
                return session_id
            if response.get("op") in [9, 429]:
                ws.close()
                return None
        ws.close()
        return None
    except:
        return None

class DiscordHuminazer:
    def __init__(self, worker_id: int) -> None:
        self.header_gen: HeaderGenerator = HeaderGenerator()
        self.profile_dir: Path = Path("io/input/profiles")
        self.avatar_dir: Path = self.profile_dir / "avatars"
        self.worker_id: int = worker_id
        self.bios: Optional[List[str]] = self._load_from_file("bio.txt")
        self.names: Optional[List[str]] = self._load_from_file("names.txt")
        self.pronouns_list: Optional[List[str]] = self._load_from_file("pronouns.txt")
        self.houses: List[str] = ["bravery", "brillance", "balance"]

    def _load_from_file(self, filename: str) -> Optional[List[str]]:
        file_path = self.profile_dir / filename
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip()]
        return None

    def _get_random_bio(self) -> Optional[str]:
        return choice(self.bios) if self.bios else None

    def _get_random_display_name(self) -> Optional[str]:
        return choice(self.names) if self.names else None

    def _get_random_pronouns(self) -> Optional[str]:
        return choice(self.pronouns_list) if self.pronouns_list else None

    def _get_random_avatar(self) -> Optional[Path]:
        avatar_files = list(self.avatar_dir.glob("*.png")) + list(self.avatar_dir.glob("*.jpg")) + list(self.avatar_dir.glob("*.jpeg"))
        return choice(avatar_files) if avatar_files else None

    def _prepare_avatar(self, path: Path) -> Optional[str]:
        try:
            with Image.open(path) as img:
                if img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (0, 0, 0))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                buffer = io.BytesIO()
                img.save(buffer, format="JPEG", quality=85)
                data = buffer.getvalue()
                
                max_bytes = 8 * 1024 * 1024
                quality = 85
                while len(data) > max_bytes and quality > 10:
                    buffer = io.BytesIO()
                    img.save(buffer, format="JPEG", quality=quality)
                    data = buffer.getvalue()
                    quality -= 10
                
                return b64encode(data).decode("utf-8")
        except:
            return None

    def humanize_account(self, token: str) -> bool:
        try:
            headers: dict = self.header_gen.generate_headers(token, location="User Profile")
            with tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True) as session:
                session.headers.update(headers)
                success = True

                bio = self._get_random_bio()
                if bio:
                    r = session.patch("https://discord.com/api/v9/users/@me", json={"bio": bio})
                    if r.status_code == 200:
                        print(f"[{self.worker_id}] {gradient_text('✓ Bio updated successfully', Neon.GRADIENT_MAGENTA)}")
                    else:
                        print(f"[{self.worker_id}] {gradient_text('✗ Failed to update bio', Neon.GRADIENT_PURPLE)}")
                        success = False

                pronouns = self._get_random_pronouns()
                if pronouns:
                    r = session.patch("https://discord.com/api/v9/users/@me", json={"pronouns": pronouns})
                    if r.status_code == 200:
                        print(f"[{self.worker_id}] {gradient_text('✓ Pronouns updated successfully', Neon.GRADIENT_MAGENTA)}")
                    else:
                        print(f"[{self.worker_id}] {gradient_text('✗ Failed to update pronouns', Neon.GRADIENT_PURPLE)}")
                        success = False

                display_name = self._get_random_display_name()
                if display_name:
                    r = session.patch("https://discord.com/api/v9/users/@me", json={"global_name": display_name})
                    if r.status_code == 200:
                        print(f"[{self.worker_id}] {gradient_text('✓ Display name updated successfully', Neon.GRADIENT_MAGENTA)}")
                    else:
                        print(f"[{self.worker_id}] {gradient_text('✗ Failed to update display name', Neon.GRADIENT_PURPLE)}")
                        success = False

                avatar_path = self._get_random_avatar()
                if avatar_path:
                    print(f"[{self.worker_id}] {gradient_text(f'⟳ Preparing avatar from {avatar_path.name}...', Neon.GRADIENT_MAGENTA)}")
                    avatar_b64 = self._prepare_avatar(avatar_path)
                    if avatar_b64:
                        session_id = get_session_id(token)
                        if session_id:
                            print(f"[{self.worker_id}] {gradient_text('⟳ Got session ID', Neon.GRADIENT_MAGENTA)}")
                            r = session.patch("https://discord.com/api/v9/users/@me", json={"avatar": f"data:image/jpeg;base64,{avatar_b64}"})
                            if r.status_code == 200:
                                print(f"[{self.worker_id}] {gradient_text('✓ Avatar updated successfully', Neon.GRADIENT_MAGENTA)}")
                            else:
                                print(f"[{self.worker_id}] {gradient_text('✗ Failed to update avatar', Neon.GRADIENT_PURPLE)}")
                                success = False
                        else:
                            print(f"[{self.worker_id}] {gradient_text('✗ Failed to get session ID', Neon.GRADIENT_PURPLE)}")
                            success = False
                    else:
                        print(f"[{self.worker_id}] {gradient_text('✗ Failed to prepare avatar', Neon.GRADIENT_PURPLE)}")
                        success = False

                house = choice(self.houses)
                house_id = self.houses.index(house) + 1
                r = session.post("https://discord.com/api/v9/hypesquad/online", json={"house_id": house_id})
                if r.status_code == 204:
                    print(f"[{self.worker_id}] {gradient_text(f'✓ Joined Hypesquad {house.capitalize()}', Neon.GRADIENT_MAGENTA)}")
                else:
                    print(f"[{self.worker_id}] {gradient_text('✗ Failed to join Hypesquad', Neon.GRADIENT_PURPLE)}")
                    success = False

                return success
        except Exception as e:
            print(f"[{self.worker_id}] {gradient_text(f'✗ Error: {str(e)}', Neon.GRADIENT_PURPLE)}")
            return False

class TokenManager:
    def __init__(self, token_file: str = "input/tokens.txt"):
        self.token_file = Path(token_file)
        self.tokens = self._load_tokens()

    def _load_tokens(self) -> List[str]:
        tokens = []
        if not self.token_file.exists():
            return []
        with open(self.token_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(':')
                if len(parts) >= 2:
                    tokens.append(parts[-1])
                else:
                    tokens.append(line)
        return tokens

def process_token(token: str, worker_id: int):
    print(f"[{worker_id}] {gradient_text(f'Processing token: {token[:20]}...', Neon.GRADIENT_MAGENTA)}")
    humanizer = DiscordHuminazer(worker_id=worker_id)
    success = humanizer.humanize_account(token)
    print(f"[{worker_id}] {gradient_text(f'Final Result: Success', Neon.GRADIENT_MAGENTA)}")
    print(f"{gradient_text('─' * 50, Neon.GRADIENT_PURPLE)}")

async def humanizer_main():
    print_banner("humanizer")
    
    token_manager = TokenManager()
    
    if not token_manager.tokens:
        print(f"{gradient_text('✗ No tokens found in input/tokens.txt!', Neon.GRADIENT_PURPLE)}")
        print(f"{gradient_text('! Please generate some accounts first using Option 1.', Neon.GRADIENT_MAGENTA)}")
        input(f"\n{gradient_text('→ Press Enter to return to main menu...', Neon.GRADIENT_MAGENTA)}")
        return
        
    print(f"{gradient_text(f'✓ Loaded {len(token_manager.tokens)} tokens', Neon.GRADIENT_MAGENTA)}")
    
    avatar_dir = Path("io/input/profiles/avatars")
    if avatar_dir.exists():
        avatar_count = len(list(avatar_dir.glob("*.png")) + list(avatar_dir.glob("*.jpg")) + list(avatar_dir.glob("*.jpeg")))
        if avatar_count > 0:
            print(f"{gradient_text(f'✓ Found {avatar_count} avatars', Neon.GRADIENT_MAGENTA)}")
        else:
            print(f"{gradient_text('! No avatars found', Neon.GRADIENT_MAGENTA)}")
    else:
        print(f"{gradient_text(f'! Avatar folder not found: {avatar_dir}', Neon.GRADIENT_MAGENTA)}")
    
    max_workers = int(input(f"\n{gradient_text('? Number of threads (1-50): ', Neon.GRADIENT_MAGENTA)}") or 10)
    max_workers = min(max_workers, 50, len(token_manager.tokens))
    
    print(f"\n{gradient_text(f'▶ Starting humanization with {max_workers} threads...', Neon.GRADIENT_MAGENTA)}\n")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for i, token in enumerate(token_manager.tokens, 1):
            futures.append(executor.submit(process_token, token, i))
        concurrent.futures.wait(futures)
    
    print(f"\n{gradient_text('✓ Humanization complete!', Neon.GRADIENT_MAGENTA)}")
    input(f"\n{gradient_text('→ Press Enter to return to main menu...', Neon.GRADIENT_MAGENTA)}")

async def generator_main():
    print_banner("generator")
    
    try:
        amount = int(input(f"{gradient_text('? How many accounts? ', Neon.GRADIENT_MAGENTA)}") or 1)
    except: 
        amount = 1

    refresh_ua_pool()
    
    for i in range(1, amount + 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("proton vpn connected✔️")
        print_banner("generator")
        print(f"{gradient_text(f'▶ Generating account {i} of {amount}', Neon.GRADIENT_MAGENTA)}\n")
        
        if not UA_POOL:
            refresh_ua_pool()
        current_ua = UA_POOL.pop()
        
        bot = DiscordBot(i, ua=current_ua)
        await bot.start()
        
        if i < amount:
            print(f"{gradient_text('⏳ Moving to next account in 5 seconds...', Neon.GRADIENT_MAGENTA)}")
            await asyncio.sleep(5)

    print(f"\n{gradient_text(f'✓ All {amount} accounts have been processed!', Neon.GRADIENT_MAGENTA)}")
    input(f"\n{gradient_text('→ Press Enter to return to main menu...', Neon.GRADIENT_MAGENTA)}")

async def main_menu():
    while True:
        print_banner("main")
        
        print(f"  {gradient_text('1 › Token Generator', Neon.GRADIENT_MAGENTA)}")
        print(f"  {gradient_text('2 › Token Humanizer', Neon.GRADIENT_MAGENTA)}")
        print(f"  {gradient_text('3 › Exit', Neon.GRADIENT_MAGENTA)}")
        print()
        
        choice = input(f"{gradient_text('→ Select option: ', Neon.GRADIENT_MAGENTA)}").strip()
        
        if choice == "1":
            await generator_main()
        elif choice == "2":
            await humanizer_main()
        elif choice == "3":
            print(f"\n{gradient_text('✗ Exiting...', Neon.GRADIENT_PURPLE)}")
            sys.exit(0)
        else:
            print(f"\n{gradient_text('✗ Invalid option!', Neon.GRADIENT_PURPLE)}")
            await asyncio.sleep(1)

if __name__ == '__main__':
    try:
        show_neon_art()
        asyncio.run(main_menu())
    except KeyboardInterrupt:
        print(f"\n{gradient_text('✗ Interrupted by user', Neon.GRADIENT_PURPLE)}")
        sys.exit()