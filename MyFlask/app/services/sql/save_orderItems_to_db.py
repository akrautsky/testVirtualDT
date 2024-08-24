from app.database import db
from datetime import datetime
from flask import current_app, jsonify
from app.models.order_items_model import OrderItem
from app.globals.global_states import global_order_items, global_order
from app.models.dataModel import OrderItem

# save_orderIems_to_db.py

def save_orderIems_to_db():
    try:
        order_items_to_save = []
        print("Processing the order items")
        print("global_order_items ::", global_order_items)
        
        for item in global_order_items:
            new_order_item = OrderItem(
                order_id=global_order.get("orderId"),
                item_id=item.get("item_id"),
                quantity=item.get("quantity"),
            )
            print('new_order_item ::', new_order_item)
            order_items_to_save.append(new_order_item)

        print("Order items to process ::", order_items_to_save)
        
        if order_items_to_save:
            db.session.add_all(order_items_to_save)  # Use add_all for multiple items
            print('Order items added to session')
            
            # Do not commit or close the session here
            return jsonify({"message": "Order Items added successfully"}), 200

        return jsonify({"message": "No order items to process"}), 200

    except Exception as e:
        print("Error occurred:", str(e))
        db.session.rollback()  # Rollback the session to avoid partial commits
        return jsonify({"error": str(e)}), 400
