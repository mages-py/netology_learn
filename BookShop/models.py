from sqlalchemy import DateTime, String, Integer, DECIMAL, Column, ForeignKey
from sqlalchemy.orm import relationship
from includes.db import Base


class Publisher(Base):
    __tablename__ = 'publishers'
    name = Column(String(100), unique=True)


class Book(Base):
    __tablename__ = 'books'
    title = Column(String(100))
    id_publisher = Column(Integer, ForeignKey('publishers.id'))
    
    publisher = relationship(Publisher, backref='books')


class Shop(Base):
    __tablename__ = 'shops'
    name = Column(String(100), unique=True)  


class Stock(Base):
    __tablename__ = 'stocks'
    id_book = Column(Integer, ForeignKey('books.id'))
    id_shop = Column(Integer, ForeignKey('shops.id'))
    count = Column(Integer)
    
    books = relationship(Book, backref='stocks')
    shops = relationship(Shop, backref='stocks')

class Sale(Base):
    __tablename__ = 'sales'
    price = Column(DECIMAL(10,2))
    date_sale = Column(DateTime)
    id_stock = Column(Integer, ForeignKey('stocks.id'))
    count = Column(Integer)
    
    stocks = relationship(Stock, backref='sales')