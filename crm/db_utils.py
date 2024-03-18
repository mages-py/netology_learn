import psycopg2 as pg
from config import SERVER, USER, PASSWORD, DATABASE, PORT

def connect():
    conn = pg.connect(database=DATABASE, user=USER, password=PASSWORD, host=SERVER, port=PORT)
    return conn


def close(conn):
        conn.close()
        

def get_sql(table_name, fields = []):
    sql = f'CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY'
    if fields:
        for field in fields:
            sql += f", {field.get('field')} {field.get('type')} {'UNIQUE' if field.get('unique', '') else ''} {'NOT NULL' if field.get('not_null', '') else ''}"
                
    sql += ')'
    return sql
    #     id SERIAL PRIMARY KEY,
    #     username TEXT UNIQUE NOT NULL,
    #     password TEXT NOT NULL,
    #     email TEXT UNIQUE NOT NULL,
    #     created TIMESTAMP DEFAULT NOW()
    # )"


def create_tables():
    # conn = connect()
    
    client = get_sql(
        table_name = 'clients', 
        fields= [
        {'field': 'first_name', 'type':'TEXT', 'not_null': True}, 
        {'field': 'last_name', 'type':'TEXT', 'not_null': True}, 
        {'field': 'email', 'type':'TEXT', 'not_null': True, 'unique': True}
        ]
    )
    
    print(client)
    
if __name__ == '__main__':
    create_tables()