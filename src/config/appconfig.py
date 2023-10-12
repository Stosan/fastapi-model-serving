# Load .env file using:
from dotenv import load_dotenv
load_dotenv()
import os

Env= os.getenv("PYTHON_ENV")
app_port = os.getenv("PORT")
auth_user = os.getenv("AUTH_USERNAME")
auth_password = os.getenv("AUTH_PASSWORD")
