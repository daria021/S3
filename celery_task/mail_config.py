from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig
import os

load_dotenv('./mail.env')

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
