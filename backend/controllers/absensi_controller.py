from flask import Blueprint, request, jsonify
from models.absensi_model import get_all_absensi, get_absensi_by_id, create_absensi, update_absensi, delete_absensi

absensi_bp = Blueprint('absensi', __name__)

@absensi_bp.route("/", methods=["GET"])
def get_absensi():
    absensi_list = get_all_absensi()
    return jsonify(absensi_list), 200

@absensi_bp.route("/<int:absensi_id>", methods=["GET"])
def get_absensi_by_id_route(absensi_id):
    absensi = get_absensi_by_id(absensi_id)
    if absensi:
        return jsonify(absensi), 200
    return jsonify({"message": "Absensi not found"}), 404

@absensi_bp.route("/", methods=["POST"])
def add_absensi():
    data = request.get_json()
    id_karyawan = data.get("id_karyawan")
    tanggal = data.get("tanggal")
    waktu_masuk = data.get("waktu_masuk")
    waktu_keluar = data.get("waktu_keluar")
    lokasi = data.get("lokasi")
    
    absensi_id = create_absensi(id_karyawan, tanggal, waktu_masuk, waktu_keluar, lokasi)
    return jsonify({"id": absensi_id, "message": "Absensi created successfully"}), 201

@absensi_bp.route("/<int:absensi_id>", methods=["PUT"])
def update_absensi_route(absensi_id):
    data = request.get_json()
    id_karyawan = data.get("id_karyawan")
    tanggal = data.get("tanggal")
    waktu_masuk = data.get("waktu_masuk")
    waktu_keluar = data.get("waktu_keluar")
    lokasi = data.get("lokasi")
    
    update_absensi(absensi_id, id_karyawan, tanggal, waktu_masuk, waktu_keluar, lokasi)
    return jsonify({"message": "Absensi updated successfully"}), 200

@absensi_bp.route("/<int:absensi_id>", methods=["DELETE"])
def delete_absensi_route(absensi_id):
    delete_absensi(absensi_id)
    return jsonify({"message": "Absensi deleted successfully"}), 200
