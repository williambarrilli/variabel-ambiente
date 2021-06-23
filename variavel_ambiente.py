import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')
PASSWORD = os.getenv('PASSWORD')

print('Host:', HOST)
print('Port:', PORT)
print('Database:', DATABASE)
print('Password:', PASSWORD)