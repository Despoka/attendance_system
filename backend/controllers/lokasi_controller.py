from flask import Blueprint, request, jsonify
from models.lokasi_model import get_all_lokasi, get_lokasi_by_id, create_lokasi, update_lokasi, delete_lokasi

lokasi_bp = Blueprint('lokasi', __name__)

@lokasi_bp.route("/", methods=["GET"])
def get_lokasi():
    lokasi_list = get_all_lokasi()
    return jsonify(lokasi_list), 200

@lokasi_bp.route("/<int:lokasi_id>", methods=["GET"])
def get_lokasi_by_id_route(lokasi_id):
    lokasi = get_lokasi_by_id(lokasi_id)
    if lokasi:
        return jsonify(lokasi), 200
    return jsonify({"message": "Lokasi not found"}), 404

@lokasi_bp.route("/", methods=["POST"])
def add_lokasi():
    data = request.get_json()
    nama_lokasi = data.get("nama_lokasi")
    
    lokasi_id = create_lokasi(nama_lokasi)
    return jsonify({"id": lokasi_id, "message": "Lokasi created successfully"}), 201

@lokasi_bp.route("/<int:lokasi_id>", methods=["PUT"])
def update_lokasi_route(lokasi_id):
    data = request.get_json()
    nama_lokasi = data.get("nama_lokasi")
    
    update_lokasi(lokasi_id, nama_lokasi)
    return jsonify({"message": "Lokasi updated successfully"}), 200

@lokasi_bp.route("/<int:lokasi_id>", methods=["DELETE"])
def delete_lokasi_route(lokasi_id):
    delete_lokasi(lokasi_id)
    return jsonify({"message": "Lokasi deleted successfully"}), 200
