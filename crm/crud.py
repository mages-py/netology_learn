from db_utils import connect, close


def create_phones(client_id:int, phones:str):
    conn= connect()
    list_phones = phones.split(',') 
    if list_phones:
        for phone in list_phones:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO phones (client_id, phone) VALUES (%s, %s)", (client_id, phone.strip()))
        try:
            conn.commit()
        finally:
            close(conn)
            
            
def delete_phone(phone_id:int):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM phones WHERE id = %s", (phone_id,))
    try:
        conn.commit()
        return True
    finally:
        close(conn)
                
            
    
def create_client(first_name: str, last_name:str, email:str, phones:str = None):
    new_id = 0
    conn = connect()
    with conn.cursor() as cur:
        cur.execute("INSERT INTO clients (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING id;", (first_name, last_name, email))  
        new_id = cur.fetchone()[0]
    try:
        conn.commit()
        if new_id and phones:
            create_phones(new_id, phones)
    finally:
        close(conn)


def update_client(client_id:int, first_name:str = None, last_name:str = None, email:str = None):
    conn = connect()
    with conn.cursor() as cur:
        if first_name:
            cur.execute("UPDATE clients SET first_name = %s WHERE id = %s", (first_name, client_id))
        if last_name:
            cur.execute("UPDATE clients SET last_name = %s WHERE id = %s", (last_name, client_id))
        if email:
            cur.execute("UPDATE clients SET email = %s WHERE id = %s", (email, client_id))
    try:
        conn.commit()
        return True
    except:
        return False
    finally:
        close(conn)


def delete_client(client_id:int):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM phones WHERE client_id = %s", (client_id,))
        cur.execute("DELETE FROM clients WHERE id = %s", (client_id,))
    try:
        conn.commit()
        return True
    except:
        return False
    finally:
        close(conn)


def get_client(first_name:str=None, last_name:str=None, email:str=None, phone:str=None):
    conn = connect()
    with conn.cursor() as cur:
        if first_name:
            cur.execute("SELECT * FROM clients WHERE first_name LIKE %s", ('%' + first_name + '%',))
        elif last_name:
            cur.execute("SELECT * FROM clients WHERE last_name LIKE %s", ('%' + last_name + '%',))
        elif email:
            cur.execute("SELECT * FROM clients WHERE email LIKE %s", ('%' + email + '%',))
        elif phone:
            cur.execute("SELECT * FROM clients WHERE id IN (SELECT client_id FROM phones WHERE phone LIKE %s)", ('%' + phone + '%',))
    try:
        return cur.fetchall()
    except:
        return None
    finally:
        close(conn)
 