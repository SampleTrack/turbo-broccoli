import os

class Config:
    API_ID = int(os.environ.get("API_ID", "12345"))
    API_HASH = os.environ.get("API_HASH", "your_hash")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_token")
    
    # Database
    MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://...")
    DB_NAME = os.environ.get("DB_NAME", "AutoMotiveBot")
    
    # Admin
    ADMIN_ID = int(os.environ.get("ADMIN_ID", "12345678"))
    
    # Render specific
    PORT = int(os.environ.get("PORT", 8080))
    
    # Version
    BOT_VERSION = "1.0.2"
    LAST_UPDATE = "Added Monetization & Riddle Logic"
