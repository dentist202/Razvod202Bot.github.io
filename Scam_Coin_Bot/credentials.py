import os
if os.path.exists(".env"):

    from dotenv import load_dotenv
    load_dotenv()


BOT_TOKEN = os.getenv('6729837745:AAGpJn--g32h8idH8gQQIchapaoKetky6V4')
BOT_USERNAME = os.getenv('Razvod202Bot')
WEBAPP_URL = os.getenv('https://dentist202.github.io/Razvod202Bot.github.io/Scam_Coin_Bot/')