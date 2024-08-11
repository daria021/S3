import asyncio


from fastapi_mail import FastMail, ConnectionConfig, MessageSchema
from dotenv import load_dotenv
import os

load_dotenv('mail.env')

mail_conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_SSL_TLS=os.getenv("MAIL_SSL_TLS").lower() in ['true', '1', 'yes'],
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

fm = FastMail(mail_conf)

message = MessageSchema(
    subject="Test Email",
    recipients=["dariaedigareva@gmail.com"],
    body="This is a test email",
    subtype="plain"
)

asyncio.run(fm.send_message(message))
