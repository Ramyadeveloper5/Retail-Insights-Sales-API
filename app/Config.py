import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('DATABASE_USERNAME')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
dbname = os.getenv('DATABASE_NAME')
secret_key = os.getenv('SECRET_KEY')
port = int(os.getenv('FLASK_PORT'))
dbport = int(os.getenv('DATABASE_PORT'))

DATABASE_URL = f"postgresql://{username}:{password}@{host}:{dbport}/{dbname}"

print(DATABASE_URL)

class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SECRET_KEY = secret_key
    PORT = port