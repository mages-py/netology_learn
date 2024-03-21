from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(int, primary_key=True)

class Publisher(Base):
    __tablename__ = 'publishers'
    
    name: Mapped[str] = mapped_column(String(100))
    
class Book(Base):
    __tablename__ = 'books'
    title: Mapped[str] = mapped_column(String(100))
    id_publisher: Mapped[int] = relationship(Publisher)

class Shop(Base):
    __tablename__ ='shops'
    name: Mapped[str] = mapped_column(String(100))
    
class Stock(Base):
    __tablename__ ='stocks'
    id_book: Mapped[int] = relationship(Book)
    id_shop: Mapped[int] = relationship(Shop)
    count: Mapped[int] = mapped_column(int)
    
    