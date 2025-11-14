from fastapi_mail import ConnectionConfig
from dotenv import load_dotenv
from pydantic import SecretStr
load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME="a71590253@gmail.com",
    MAIL_PASSWORD=SecretStr("qajh pyda pjmv imza"),
    MAIL_FROM="a71590253@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    # MAIL_TLS=True,
    # MAIL_SSL=False
    USE_CREDENTIALS=True
)



