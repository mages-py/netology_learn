from includes.config import USER, PASSWORD, SERVER, PORT, DATABASE
from sqlalchemy import create_engine, Integer, Column
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{SERVER}:{PORT}/{DATABASE}')
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)

    
def create_db():
    Base.metadata.create_all(engine)


def destroy_db():
    Base.metadata.drop_all(engine)
