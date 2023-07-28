from twilio.rest import Client
import os

class NotificationManager:
    def __init__(self):
        self.account_sid = os.getenv("twillo_account_sid")
        self.auth_token = os.getenv("twillo_auth_token")


    def send_message(self,message:str):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            from_='+12342399381',
            body=message,
            to='+48664893447'
        )
