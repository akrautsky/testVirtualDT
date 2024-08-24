from flask import Blueprint, jsonify, request
from app.globals.global_states import global_order, global_order_items
from app.events.order_summary_event import emit_order_summary_event
from app.services.sql.save_orderItems_to_db import save_orderIems_to_db
from app.services.sql.save_order_to_db import save_order_to_db
from app.database import db
from app.models.order_model import Order
from app.models.order_items_model import OrderItem


def getOrderTotal(orderTotal, tip):
    return orderTotal + tip 

process_my_tip_bp = Blueprint('processMyTip', __name__)
@process_my_tip_bp.route('/processMyTip', methods=['POST'])
def processMyTip():

    if request.is_json:
        data = request.get_json()
        charity_amount = 0
        tipAmount = 0
        orderTotal = 0
        # Extract tool info
        toolCalls = data.get('message', {}).get('toolCalls', [])
        result = []

        for toolCall in toolCalls:
            toolCallId = toolCall.get('id', 'unknown')
            arguments = toolCall.get('function', {}).get('arguments', {})
            tip = arguments.get('tip', {})
            tipAmount = tip.get('tip', 0)
            orderTotal =  global_order.get('total', 0)
            
            print('Order total from the vapi ::', orderTotal)

            if orderTotal is not None and tipAmount is not None:
                orderTotal = getOrderTotal(orderTotal, tipAmount)
            if tip.get('roundofftotal'):
                charity_amount = round(orderTotal) - orderTotal
                orderTotal = round(orderTotal)

            result.append({
                "toolCallId": toolCallId,
                "result": f"Order Total with tip : {orderTotal}"
            })
        
        global_order['tip_amount'] = tipAmount
        global_order['roundedDollar'] = charity_amount
        global_order['total'] = orderTotal



        print('global_order ::', global_order)
        print('global_order_items ::', global_order_items)

        resultJson = {"results": result}
        print('resultJson ::', resultJson)

        # emit the order summary event
        emit_order_summary_event()

        # todo:: make this asynch in different thread for better optimization
        # call the database to save order and order items
        save_order_to_db()
        # order = OrderItem.query.get(1) 
        # db.session.refresh(order)
        
        #save_orderIems_to_db()

        return jsonify(resultJson)
    else:
        return jsonify({"error": "Request is not JSON"}), 400