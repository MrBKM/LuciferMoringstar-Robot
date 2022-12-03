# MIT License
# Copyright (c) 2022 Muhammed
import os, re
search = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Creator
CREATOR_NAME = os.environ.get("CREATOR_NAME", "Bikash")
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "Bikash_9999")

# Account
API_HASH = os.environ.get("API_HASH", "8719d11809492f836004a39b42599215")
API_ID = os.environ.get("API_ID", "12694006")
# About Bot
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5567354112:AAH3f9bi60I8HiZ5mCu38-mBeMCkdd62T1I")
PICS = os.environ.get("PICS", "https://telegra.ph/file/913f9af3d11d8c0306043.jpg")
# Database
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Balmiki")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Balmiki:Balmiki@cluster0.lmden.mongodb.net/?retryWrites=true&w=majority")
# Chats & Users
ADMINS = os.environ.get("ADMINS", "953377581 5630723610")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "Tk_movies_adda")
AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1001506877410")
CHANNELS = [int(ch) if search.search(ch) else ch for ch in os.environ.get("CHANNELS", "-1001822275183").split()]
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001646581413")
GET_FILECHANNEL = os.environ.get("GET_FILECHANNEL", "-1001576725431")
FILTER_DEL_SECOND = int(os.environ.get("FILTER_DEL_SECOND", "600"))

# AutoFilter
AUTH_GROUPS = os.environ.get("AUTH_GROUPS", "-1001510283128")
AUTH_USERS = [int(user) if search.search(user) else user for user in os.environ.get('AUTH_USERS', '953377581 5630723610').split()]
FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10")
PROTECT_FILES = is_enabled((os.environ.get('PROTECT_FILES', "True")), True) 
