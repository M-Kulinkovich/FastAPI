from dotenv import load_dotenv
import os


load_dotenv()

USER_DB = os.environ.get('USER_DB')
PASS_DB = os.environ.get('PASS_DB')
HOST_DB = os.environ.get('HOST_DB')
PORT_DB = os.environ.get('PORT_DB')
NAME_DB = os.environ.get('NAME_DB')

SECRET_JWT = os.environ.get('SECRET_JWT')
