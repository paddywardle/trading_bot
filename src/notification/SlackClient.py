from src.notification.Message import Message
from src.requests.HTTPRequests import HTTPRequests

import requests as req
from dotenv import load_dotenv
import os

class SlackClient:

    def __init__(self) -> None:
        load_dotenv("config/.env")
        self.slack_webhook = os.getenv("SLACK_WEBHOOK")

    def send_message(self, mes:str=""):

        message = Message(mes)
        resp = HTTPRequests.post(self.slack_webhook, data = message.payload)

        return resp
        

