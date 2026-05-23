import os
from dotenv import load_dotenv

load_dotenv("python/env/.env")

def get_env_required(name: str) -> str:
    value = os.getenv(name)

    if value is None or value.strip() == "":
        raise RuntimeError(f"Variabile mancante nel .env: {name}")

    return value

