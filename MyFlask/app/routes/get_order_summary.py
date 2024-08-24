from flask import Blueprint, jsonify

get_Order_Summary_bp = Blueprint('getOrderSummary', __name__)

@get_Order_Summary_bp.route('/getOrderSummary', methods=['GET'])
def getOrderSummary():
    orderSummary = [
        {"total": 128.5,
        "tip":12,
        "tax": 8,
        "rounded$": True,
        "grandTotal": 148.5}
    ]

    return jsonify({"orderSummary": orderSummary})