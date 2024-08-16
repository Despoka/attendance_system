from config import create_connection

def get_all_absensi():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM absensi")
    absensi_list = cur.fetchall()
    cur.close()
    conn.close()
    return absensi_list

def get_absensi_by_id(absensi_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM absensi WHERE ID_Absensi = %s", (absensi_id,))
    absensi = cur.fetchone()
    cur.close()
    conn.close()
    return absensi

def create_absensi(id_karyawan, tanggal, waktu_masuk, waktu_keluar, lokasi):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO absensi (ID_Karyawan, Tanggal, Waktu_Masuk, Waktu_Keluar, Lokasi) VALUES (%s, %s, %s, %s, %s) RETURNING ID_Absensi", 
                (id_karyawan, tanggal, waktu_masuk, waktu_keluar, lokasi))
    absensi_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return absensi_id

def update_absensi(absensi_id, id_karyawan, tanggal, waktu_masuk, waktu_keluar, lokasi):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE absensi SET ID_Karyawan = %s, Tanggal = %s, Waktu_Masuk = %s, Waktu_Keluar = %s, Lokasi = %s WHERE ID_Absensi = %s",
                (id_karyawan, tanggal, waktu_masuk, waktu_keluar, lokasi, absensi_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_absensi(absensi_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM absensi WHERE ID_Absensi = %s", (absensi_id,))
    conn.commit()
    cur.close()
    conn.close()
