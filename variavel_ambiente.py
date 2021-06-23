import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')
PASSWORD = os.getenv('PASSWORD')

while True:
    senha = input('digite a senha:')
    if(senha == PASSWORD): {
        print('senha aceita')
    }
