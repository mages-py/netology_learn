from sqlalchemy import DateTime, String, Integer, DECIMAL, Column, ForeignKey
from sqlalchemy.orm import relationship
from includes.db import Base


class Publisher(Base):
    __tablename__ = 'publisher'
    name = Column(String(100), unique=True)


class Book(Base):
    __tablename__ = 'book'
    title = Column(String(100))
    id_publisher = Column(Integer, ForeignKey('publisher.id'))

    publisher = relationship(Publisher, backref='books')


class Shop(Base):
    __tablename__ = 'shop'
    name = Column(String(100), unique=True)


class Stock(Base):
    __tablename__ = 'stock'
    id_book = Column(Integer, ForeignKey('book.id'))
    id_shop = Column(Integer, ForeignKey('shop.id'))
    count = Column(Integer)

    books = relationship(Book, backref='stock')
    shops = relationship(Shop, backref='stock')


class Sale(Base):
    __tablename__ = 'sale'
    price = Column(DECIMAL(10, 2))
    date_sale = Column(DateTime)
    id_stock = Column(Integer, ForeignKey('stock.id'))
    count = Column(Integer)

    stocks = relationship(Stock, backref='sales')
