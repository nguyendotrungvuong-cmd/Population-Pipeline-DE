import os
from pathlib import Path
from dotenv import load_dotenv

dir = Path(__file__).resolve().parent.parent
load_dotenv(dir / ".env")
API_URL = "https://api.api-ninjas.com/v1/population"


def get_api_key():
    api_key = os.getenv("API_NINJAS_KEY")
    if not api_key:
        raise ValueError("MISSING API_KEY")
    return api_key
