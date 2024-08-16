from flask import Blueprint, request, jsonify
from models.karyawan_model import get_all_karyawan, get_karyawan_by_id, create_karyawan, update_karyawan, delete_karyawan

karyawan_bp = Blueprint('karyawan', __name__)

@karyawan_bp.route("/", methods=["GET"])
def get_karyawan():
    karyawan_list = get_all_karyawan()
    return jsonify(karyawan_list), 200

@karyawan_bp.route("/<int:karyawan_id>", methods=["GET"])
def get_karyawan_by_id_route(karyawan_id):
    karyawan = get_karyawan_by_id(karyawan_id)
    if karyawan:
        return jsonify(karyawan), 200
    return jsonify({"message": "Karyawan not found"}), 404

@karyawan_bp.route("/", methods=["POST"])
def add_karyawan():
    data = request.get_json()
    kode_karyawan = data.get("kode_karyawan")
    nama = data.get("nama")
    jabatan = data.get("jabatan")
    
    karyawan_id = create_karyawan(kode_karyawan, nama, jabatan)
    return jsonify({"id": karyawan_id, "message": "Karyawan created successfully"}), 201

@karyawan_bp.route("/<int:karyawan_id>", methods=["PUT"])
def update_karyawan_route(karyawan_id):
    data = request.get_json()
    kode_karyawan = data.get("kode_karyawan")
    nama = data.get("nama")
    jabatan = data.get("jabatan")
    
    update_karyawan(karyawan_id, kode_karyawan, nama, jabatan)
    return jsonify({"message": "Karyawan updated successfully"}), 200

@karyawan_bp.route("/<int:karyawan_id>", methods=["DELETE"])
def delete_karyawan_route(karyawan_id):
    delete_karyawan(karyawan_id)
    return jsonify({"message": "Karyawan deleted successfully"}), 200
