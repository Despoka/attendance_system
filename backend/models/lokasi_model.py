from config import create_connection

def get_all_lokasi():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM lokasi")
    lokasi_list = cur.fetchall()
    cur.close()
    conn.close()
    return lokasi_list

def get_lokasi_by_id(lokasi_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM lokasi WHERE ID_Lokasi = %s", (lokasi_id,))
    lokasi = cur.fetchone()
    cur.close()
    conn.close()
    return lokasi

def create_lokasi(nama_lokasi):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO lokasi (Nama_Lokasi) VALUES (%s) RETURNING ID_Lokasi", 
                (nama_lokasi,))
    lokasi_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return lokasi_id

def update_lokasi(lokasi_id, nama_lokasi):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE lokasi SET Nama_Lokasi = %s WHERE ID_Lokasi = %s",
                (nama_lokasi, lokasi_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_lokasi(lokasi_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM lokasi WHERE ID_Lokasi = %s", (lokasi_id,))
    conn.commit()
    cur.close()
    conn.close()
