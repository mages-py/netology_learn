import psycopg2 as pg
from config import SERVER, USER, PASSWORD, DATABASE, PORT

def connect():
    conn = pg.connect(database=DATABASE, user=USER, password=PASSWORD, host=SERVER, port=PORT)
    return conn


def close(conn):
        conn.close()

def _delete_table(table_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS " + table_name)
    conn.commit()
    close(conn)


def create_tables():
    _delete_table('phones')
    _delete_table('clients')
    
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id SERIAL PRIMARY KEY,
                first_name TEXT UNIQUE NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL);
        """)
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phones (
                id SERIAL PRIMARY KEY,
                client_id BIGINT NOT NULL,
                phone TEXT NOT NULL);
            """)
        
        cur.execute("ALTER TABLE phones ADD FOREIGN KEY (client_id) REFERENCES clients(id);")
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    create_tables()