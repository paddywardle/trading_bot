from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv
import os
import sys

@dataclass
class AlpacaKeys:

    api_key:str
    secret_key:str

    def __init__(self) -> None:
        load_dotenv("config/.env")
        self.api_key = os.getenv("ALPACA_API_KEY")
        self.secret_key = os.getenv("ALPACA_SECRET")