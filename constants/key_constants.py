import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

SECRETKEY = os.getenv('SECRETKEY')
JWTALGO = os.getenv('JWTALGO')
DATABASE_URL = os.getenv('DATABASE_URL')