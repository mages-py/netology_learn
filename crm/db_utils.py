import psycopg2 as pg
from config import SERVER, USER, PASSWORD, DATABASE, PORT


def connect():
    conn = pg.connect(database=DATABASE, user=USER,
                      password=PASSWORD, host=SERVER, port=PORT)
    return conn


def close(conn):
    conn.close()


def _delete_table(table_name: str):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS " + table_name)
    try:
        conn.commit()
    finally:
        conn.close()


def create_tables():
    _delete_table('phones')
    _delete_table('clients')

    conn = connect()
    with conn.cursor() as cur:
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

        cur.execute(
            "ALTER TABLE phones ADD FOREIGN KEY (client_id) REFERENCES clients(id);")
    try:
        conn.commit()
    finally:
        conn.close()


if __name__ == '__main__':
    create_tables()
