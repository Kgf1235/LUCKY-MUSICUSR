# KAAL X - Telegram Projects
# (c) 2022 - 2023 KAAL
# Don't Kang Bitch -! 

import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters



if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v0.1"

# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
ALIVE_MSG = os.getenv("ALIVE_MSG", "")
PING_MSG = os.getenv("PING_MSG", "")
SESSION = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
TIMEZONE = os.environ.get("TIMEZONE", "Asia/Kolkata")
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)
MONGO_DB = os.environ.get("MONGO_DB", "")
    
HNDLR = os.getenv("HNDLR", ".")
sudo = os.getenv("SUDO_USERS")

SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)




# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817").split())))
#----------------------------------------------



app = Client(
    name="[Meow]",
    session_string=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
    plugins={'root': 'Meow.Modules'}
)
print("Client 1 Found")

app2 = Client(
    name="[Meow]",
    session_string=SESSION2,
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
    plugins={'root': 'Meow.Modules'}
)
print("Client 2 Found")
else:
    app2 = None

app3 = Client(
    name="[Meow]",
    session_string=SESSION3,
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
    plugins={'root': 'Meow.Modules'}
)
print("Client 3 Found")
else:
    app3 = None

app4 = Client(
    name="[Meow]",
    session_string=SESSION4,
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
    plugins={'root': 'Meow.Modules'}
)
print("Client 4 Found")
else:
    app4 = None

app5 = Client(
    name="[Meow]",
    session_string=SESSION5,
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
    plugins={'root': 'Meow.Modules'}
)
print("Client 5 Found")
else:
    app5 = None




hl = HNDLR[0]
start_time = time.time()

#-------------------------CLIENTS-----------------------------



