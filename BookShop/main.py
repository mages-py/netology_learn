from models import Publisher, Book, Shop, Stock, Sale
from includes.db import create_db, destroy_db, Session


def get_sales_for_publisher(publisher):
    session = Session()
    results =session.query(
        Book.title, 
        Shop.name, 
        Sale.price, 
        Sale.date_sale) \
            .join(Publisher).join(Shop).join(Stock).join(Sale) \
            .filter(Publisher.name.ilike('%' + publisher + '%')).all()
    
    # .join(
    #     Shop).join(Sale).join(Publisher).filter(Publisher.name.ilike('%' + publisher + '%')).all()
    
    return results


if __name__ == "__main__":
    ...
    q = get_sales_for_publisher('пушкин')
    print(q)
    # destroy_db()
    # create_db()
