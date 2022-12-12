import os
from os.path import join

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = join(BASE_DIR, '.env.dev')
AWS_REGION = os.getenv('AWS_REGION')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
DYNAMO_ENDPOINT = os.getenv('DYNAMO_ENDPOINT')
RABBIT_USERNAME = os.getenv('RABBIT_USERNAME')
RABBIT_PASSWORD = os.getenv('RABBIT_PASSWORD')
RABBIT_HOST = os.getenv('RABBIT_HOST')
RABBIT_PORT = os.getenv('RABBIT_PORT')