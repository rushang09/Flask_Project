# app/routes.py

from flask import Blueprint, request, jsonify
from app import db
from app.models import Item

main = Blueprint('main', __name__)

@main.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'name': item.name, 'description': item.description} for item in items])

@main.route('/item', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data['description'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item created successfully!'}), 201

@main.route('/item/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    item = Item.query.get_or_404(id)
    item.name = data['name']
    item.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Item updated successfully!'})

@main.route('/item/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully!'})
