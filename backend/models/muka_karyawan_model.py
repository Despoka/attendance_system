from config import create_connection

def get_all_muka_karyawan():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mukaKaryawan")
    muka_karyawan_list = cur.fetchall()
    cur.close()
    conn.close()
    return muka_karyawan_list

def get_muka_karyawan_by_id(muka_karyawan_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mukaKaryawan WHERE ID_Muka = %s", (muka_karyawan_id,))
    muka_karyawan = cur.fetchone()
    cur.close()
    conn.close()
    return muka_karyawan

def create_muka_karyawan(id_karyawan, nama_file_muka):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO mukaKaryawan (ID_Karyawan, Nama_File_Muka) VALUES (%s, %s) RETURNING ID_Muka", 
                (id_karyawan, nama_file_muka))
    muka_karyawan_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return muka_karyawan_id

def update_muka_karyawan(muka_karyawan_id, id_karyawan, nama_file_muka):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE mukaKaryawan SET ID_Karyawan = %s, Nama_File_Muka = %s WHERE ID_Muka = %s",
                (id_karyawan, nama_file_muka, muka_karyawan_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_muka_karyawan(muka_karyawan_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM mukaKaryawan WHERE ID_Muka = %s", (muka_karyawan_id,))
    conn.commit()
    cur.close()
    conn.close()
