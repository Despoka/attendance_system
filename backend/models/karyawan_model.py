from config import create_connection

def get_all_karyawan():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM karyawan")
    karyawan_list = cur.fetchall()
    cur.close()
    conn.close()
    return karyawan_list

def get_karyawan_by_id(karyawan_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM karyawan WHERE ID_Karyawan = %s", (karyawan_id,))
    karyawan = cur.fetchone()
    cur.close()
    conn.close()
    return karyawan

def create_karyawan(kode_karyawan, nama, jabatan):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO karyawan (Kode_Karyawan, Nama, Jabatan) VALUES (%s, %s, %s) RETURNING ID_Karyawan", 
                (kode_karyawan, nama, jabatan))
    karyawan_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return karyawan_id

def update_karyawan(karyawan_id, kode_karyawan, nama, jabatan):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE karyawan SET Kode_Karyawan = %s, Nama = %s, Jabatan = %s WHERE ID_Karyawan = %s",
                (kode_karyawan, nama, jabatan, karyawan_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_karyawan(karyawan_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM karyawan WHERE ID_Karyawan = %s", (karyawan_id,))
    conn.commit()
    cur.close()
    conn.close()
