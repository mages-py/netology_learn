from includes.config import USER, PASSWORD, SERVER, PORT, DATABASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DSN = f'postgresql+psycopg2://{USER}:{PASSWORD}@{SERVER}:{PORT}/{DATABASE}'
engine = create_engine(DSN)

def get_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
