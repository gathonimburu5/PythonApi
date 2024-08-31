from decouple import config
from urllib.parse import quote
import os

class DevConfig():
    password = quote('@Paulmburu5')
    db_uri = f'postgresql://postgres:{password}@localhost/BooksDb'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', db_uri)
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = True
    

