import os


# Config file for the application
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Auth:
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    TENANT_ID = os.environ.get("TENANT_ID")  # Add this
    AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
    REDIRECT_URL = os.environ.get("REDIRECT_URL")
