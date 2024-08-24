from flask import Blueprint, jsonify
from flask_cors import CORS


get_my_order_bp = Blueprint('myOrder', __name__)

@get_my_order_bp.route('/getMyOrder', methods=['GET'])
def getMyOrder():
    
    myOrder = [
        {"item": "Margherita Pizza", "quantity": 2},
        {"item": "Ice Cream", "quantity": 4},
        {"item": "Pasta Alfredo", "quantity": 1},
        {"item": "Caesar Salad", "quantity": 3},
        {"item": "Garlic Bread", "quantity": 5},
        {"item": "Mushroom Soup", "quantity": 2},
        {"item": "Apple Pie", "quantity": 3}
    ]

    return jsonify({"myOrder": myOrder})