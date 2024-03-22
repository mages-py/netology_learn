from models import Publisher, Book, Shop, Stock, Sale
from includes.db import create_db, destroy_db

# https://github.com/MADTeacher/MADPythonCourse/blob/master/sqlalchemy%2Bsqlite_create%20db%20and%20tables/models/database.py
    
if __name__ == "__main__":
    # destroy_db()
    create_db()