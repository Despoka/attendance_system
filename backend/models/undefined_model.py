from config import create_connection

def get_all_undefined():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM undefined")
    undefined_list = cur.fetchall()
    cur.close()
    conn.close()
    return undefined_list

def get_undefined_by_id(undefined_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM undefined WHERE ID_Undefined = %s", (undefined_id,))
    undefined = cur.fetchone()
    cur.close()
    conn.close()
    return undefined

def create_undefined(deskripsi):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO undefined (Deskripsi) VALUES (%s) RETURNING ID_Undefined", 
                (deskripsi,))
    undefined_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return undefined_id

def update_undefined(undefined_id, deskripsi):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE undefined SET Deskripsi = %s WHERE ID_Undefined = %s",
                (deskripsi, undefined_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_undefined(undefined_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM undefined WHERE ID_Undefined = %s", (undefined_id,))
    conn.commit()
    cur.close()
    conn.close()
