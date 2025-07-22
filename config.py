import os

API_ID = int(os.getenv("API_ID", 12345))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
MONGO_URL = os.getenv("MONGO_URL", "your_mongo_uri")
ADMIN_ID = int(os.getenv("ADMIN_ID", 12345678))
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "yourchannel")
