from flask import Blueprint, request, jsonify
from models.undefined_model import get_all_undefined, get_undefined_by_id, create_undefined, update_undefined, delete_undefined

undefined_bp = Blueprint('undefined', __name__)

@undefined_bp.route("/", methods=["GET"])
def get_undefined():
    undefined_list = get_all_undefined()
    return jsonify(undefined_list), 200

@undefined_bp.route("/<int:undefined_id>", methods=["GET"])
def get_undefined_by_id_route(undefined_id):
    undefined = get_undefined_by_id(undefined_id)
    if undefined:
        return jsonify(undefined), 200
    return jsonify({"message": "Undefined not found"}), 404

@undefined_bp.route("/", methods=["POST"])
def add_undefined():
    data = request.get_json()
    deskripsi = data.get("deskripsi")
    
    undefined_id = create_undefined(deskripsi)
    return jsonify({"id": undefined_id, "message": "Undefined created successfully"}), 201

@undefined_bp.route("/<int:undefined_id>", methods=["PUT"])
def update_undefined_route(undefined_id):
    data = request.get_json()
    deskripsi = data.get("deskripsi")
    
    update_undefined(undefined_id, deskripsi)
    return jsonify({"message": "Undefined updated successfully"}), 200

@undefined_bp.route("/<int:undefined_id>", methods=["DELETE"])
def delete_undefined_route(undefined_id):
    delete_undefined(undefined_id)
    return jsonify({"message": "Undefined deleted successfully"}), 200
