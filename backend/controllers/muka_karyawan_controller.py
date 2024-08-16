from flask import Blueprint, request, jsonify
from models.muka_karyawan_model import get_all_muka_karyawan, get_muka_karyawan_by_id, create_muka_karyawan, update_muka_karyawan, delete_muka_karyawan

muka_karyawan_bp = Blueprint('muka_karyawan', __name__)

@muka_karyawan_bp.route("/", methods=["GET"])
def get_muka_karyawan():
    muka_karyawan_list = get_all_muka_karyawan()
    return jsonify(muka_karyawan_list), 200

@muka_karyawan_bp.route("/<int:muka_karyawan_id>", methods=["GET"])
def get_muka_karyawan_by_id_route(muka_karyawan_id):
    muka_karyawan = get_muka_karyawan_by_id(muka_karyawan_id)
    if muka_karyawan:
        return jsonify(muka_karyawan), 200
    return jsonify({"message": "Muka Karyawan not found"}), 404

@muka_karyawan_bp.route("/", methods=["POST"])
def add_muka_karyawan():
    data = request.get_json()
    id_karyawan = data.get("id_karyawan")
    nama_file_muka = data.get("nama_file_muka")
    
    muka_karyawan_id = create_muka_karyawan(id_karyawan, nama_file_muka)
    return jsonify({"id": muka_karyawan_id, "message": "Muka Karyawan created successfully"}), 201

@muka_karyawan_bp.route("/<int:muka_karyawan_id>", methods=["PUT"])
def update_muka_karyawan_route(muka_karyawan_id):
    data = request.get_json()
    id_karyawan = data.get("id_karyawan")
    nama_file_muka = data.get("nama_file_muka")
    
    update_muka_karyawan(muka_karyawan_id, id_karyawan, nama_file_muka)
    return jsonify({"message": "Muka Karyawan updated successfully"}), 200

@muka_karyawan_bp.route("/<int:muka_karyawan_id>", methods=["DELETE"])
def delete_muka_karyawan_route(muka_karyawan_id):
    delete_muka_karyawan(muka_karyawan_id)
    return jsonify({"message": "Muka Karyawan deleted successfully"}), 200
