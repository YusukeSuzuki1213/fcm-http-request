import os
from dotenv import load_dotenv

load_dotenv("./.env")
PROJECT_ID = os.getenv("PROJECT_ID")
FIREBASE_DEVICE_TOKEN = os.getenv("FIREBASE_DEVICE_TOKEN")
