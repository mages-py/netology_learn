import json
from prettytable import PrettyTable
from models import Publisher, Book, Shop, Stock, Sale
from includes.db import Session

MODELS = {
    'publisher': Publisher,
    'book': Book,
    'shop': Shop,
    'stock': Stock,
    'sale': Sale
}


def insert_data_from_json():
    with open('assets/tests_data.json', encoding='utf-8') as f:
        data = json.load(f)

    session = Session()
    try:
        for row in data:
            model = MODELS[row['model']]
            session.add(model(id=row['pk'], **row['fields']))
            session.commit()
    finally:
        session.close()


def get_sales_for_publisher(publisher):
    session = Session()

    try:
        subq = session.query(Book).join(Publisher).filter(
            Publisher.name.ilike('%' + publisher + '%')).subquery('publisher_books')
        results = session.query(
            subq.c.title.label('book title'),
            Shop.name.label('shop_name'),
            Sale.price.label('sale_price'),
            Sale.date_sale.label('sale_date')
        ).select_from(Shop).join(Stock).join(Sale).join(subq, Stock.id_book == subq.c.id).all()
        return results
    finally:
        session.close()


if __name__ == "__main__":
    # Функция для заполнения БД тестовыми данными
    # insert_data_from_json()

    # Функция для вывода данных о продажах книг в магазинах определенного автора
    publisher = input('Введите название автора: ')
    q = get_sales_for_publisher(publisher)

    # Вывод данных в таблицу
    if q:
        tbl = PrettyTable()
        tbl.field_names = [
            'Название книги', 'Название магазина, в котором была куплена эта книга', 'Стоимость покупки', 'Дата покупки']
        for row in q:
            tbl.add_row([*row])
        print(tbl)
