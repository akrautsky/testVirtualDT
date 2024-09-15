from app.database import db
from datetime import datetime
from flask import current_app, jsonify
from app.models.order_model import Order
from app.globals.global_states import global_order_items, global_order
from app.services.sql.save_orderItems_to_db import save_orderIems_to_db
from sqlalchemy import text
from datetime import datetime
from app.models.dataModel import Order
# save_order_to_db.py

def save_order_to_db():
    try:
        print('global_order :: in db', global_order)

        new_order = Order(
            order_total=global_order.get("total", 0),
            order_date=datetime.now(),  
            total_items=global_order.get("totalItems", 0),  
            tip_amount=global_order.get("tip_amount", 0.0),
            roundedDollar=global_order.get("roundedDollar", 0.0)
        )
        
        print('Order instantiated:', new_order)

        db.session.add(new_order)
        print('Order added to session:', new_order)

        db.session.commit()
        print('Session committed for Order')

        db.session.refresh(new_order)
        print('Order refreshed from database:', new_order)

        global_order['orderId'] = new_order.order_id
        print('Order ID set:', global_order['orderId'])

        print('Gobal orders::', global_order)
        print('Gloabl order items::', global_order_items)
        # Process the order items; session commit is handled hereafter
        save_orderIems_to_db()

        # Commit after adding order items
        db.session.commit()
        print('Session committed for Order Items')

        # clear the global variables for the next order
        global_order.clear()
        global_order_items.clear()

        # todo:: check whats the best practice the session to close
        

        return jsonify({"message": "Order saved successfully"}), 200

    except Exception as e:
        print("Error occurred:", str(e))
        db.session.rollback()  # Rollback the session to avoid partial commits
        return jsonify({"error": str(e)}), 400

    finally:
        db.session.close()  # Ensure that the session is closed after all operations




def check_db_connection():
    try:
        # Run a simple query to check the connection
        result = db.session.execute(text("SELECT 1"))
        print("Connected to the database successfully!")
        return True
    except Exception as e:
        print("Failed to connect to the database.")
        print("Error:", e)
        return False