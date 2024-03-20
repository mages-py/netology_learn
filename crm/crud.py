from db_utils import connect, close


def create_phones(client_id: int, phones: str):

    list_phones = phones.split(',')
    cur_phones = [phone[1] for phone in get_phones(client_id)]
    if list_phones:
        conn = connect()
        try:
            for phone in list_phones:
                if phone not in cur_phones:
                    with conn.cursor() as cur:
                        cur.execute(
                            "INSERT INTO phones (client_id, phone) VALUES (%s, %s)", (client_id, phone.strip()))
                    conn.commit()
            return True
        finally:
            close(conn)


def get_phones(client_id: int):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, phone FROM phones WHERE client_id=%s", (client_id,))
        phones = cur.fetchall()
    close(conn)
    return phones


def delete_phones(phone_id: int = None, client_id: int = None):
    conn = connect()
    try:
        with conn.cursor() as cur:
            if phone_id:
                cur.execute("DELETE FROM phones WHERE id = %s", (phone_id,))
            elif client_id:
                cur.execute(
                    "DELETE FROM phones WHERE client_id = %s", (client_id,))
            else:
                raise ValueError('Необходимо указать id или client_id')
        conn.commit()
        return True
    finally:
        close(conn)


def create_client(first_name: str, last_name: str, email: str, phones: str = None):
    new_id = 0
    cur_client = get_client(email=email)
    if cur_client:
        print('Клиент с таким email уже существует')
        return False

    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO clients (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING id;",
                        (first_name, last_name, email))
            new_id = cur.fetchone()[0]

        conn.commit()
        if new_id and phones:
            create_phones(new_id, phones)
        return new_id
    finally:
        close(conn)


def update_client(client_id: int, first_name: str = None, last_name: str = None, email: str = None, phones: str = None):
    conn = connect()

    try:
        with conn.cursor() as cur:
            if first_name:
                cur.execute(
                    "UPDATE clients SET first_name = %s WHERE id = %s", (first_name, client_id))

            if last_name:
                cur.execute(
                    "UPDATE clients SET last_name = %s WHERE id = %s", (last_name, client_id))

            if email:
                cur.execute(
                    "UPDATE clients SET email = %s WHERE id = %s", (email, client_id))
        conn.commit()

        if phones:
            create_phones(client_id, phones)
        return True
    finally:
        close(conn)


def delete_client(client_id: int):
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM phones WHERE client_id = %s", (client_id,))
            cur.execute("DELETE FROM clients WHERE id = %s", (client_id,))
        conn.commit()
        return True
    finally:
        close(conn)


def get_client(id: int = None, first_name: str = None, last_name: str = None, email: str = None, phone: str = None):
    conn = connect()
    try:
        with conn.cursor() as cur:
            if id:
                cur.execute(
                    "SELECT * FROM clients WHERE id = %s ORDER BY id", (id,))
            elif first_name:
                cur.execute(
                    "SELECT * FROM clients WHERE first_name = %s ORDER BY id", (first_name,))
            elif last_name:
                cur.execute(
                    "SELECT * FROM clients WHERE last_name = %s ORDER BY id", (last_name,))
            elif email:
                cur.execute(
                    "SELECT * FROM clients WHERE email = %s ORDER BY id", (email,))
            elif phone:
                cur.execute(
                    "SELECT * FROM clients WHERE id IN (SELECT client_id FROM phones WHERE phone = %s) ORDER BY id", (phone,))
            else:
                cur.execute("SELECT * FROM clients ORDER BY id")
            return cur.fetchall()
    finally:
        close(conn)
