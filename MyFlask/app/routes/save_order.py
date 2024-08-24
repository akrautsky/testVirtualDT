from flask import Blueprint, request, jsonify, current_app
from app.database import db
from app.models.order_model import Order
from datetime import datetime

save_order_bp  = Blueprint('saveOrder', __name__)

@save_order_bp.route('/saveOrder', methods=['POST'])
def saveOrder():
    try:
        data = request.get_json()
        
        # get the data from request
        total = data.get('total')
        new_order = Order(
            total=total,
            dateoforder=datetime.now()
        )

        # Adding data to database session
        db.session.add(new_order)
        db.session.commit()


        # save to firebase database
        firestore_db = current_app.firebase_db
        doc_ref = firestore_db.collection('orders').document()  # Create or access 'orders' collection
        doc_ref.set({
            'total': data['total'],
            'dateoforder': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

        return jsonify({"message": "Order saved successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400