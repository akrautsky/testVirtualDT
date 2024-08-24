from flask import Blueprint, jsonify, request
import json
from app.services.sql.save_order_to_db import save_order_to_db
from app.globals.global_states import global_order, global_order_items
from datetime import datetime
from app.events.current_order_event import emit_current_order_event


# accessing the menu
with open('app/menu.json') as f:
    menu = json.load(f)


def getPriceFromMenu(itemName):
    global menu

    for item in menu:
        if item['name'].lower() == itemName.lower():
            return item['price']


def getTotal(orderJson):
    global menu
    orderTotal = 0
    print('Order: ' + str(orderJson))
    if isinstance(orderJson, dict):
        orderJson = [orderJson]
    else:
        orderJson = orderJson
    
    # set the items size
    global_order['totalItems'] = len(orderJson)

    for item in orderJson:
        # collect the order items to save to database
        global_order_items.append(item)


        price = getPriceFromMenu(item['item'])
        if price is not None:
            orderTotal += price * item['quantity']
            print('Order Total: ' + str(orderTotal) + ' for ' + str(item['quantity']) + ' ' + str(item['item']))
            
    print('global_order_items from processMyorder::', global_order_items)
    return orderTotal
            

process_my_order_bp = Blueprint('processMyOrder', __name__)
@process_my_order_bp.route('/processMyOrder', methods=['POST'])
def processMyOrder():
    if request.is_json:
        data = request.get_json()
        print('data ::', data)
        # Extract toolCallId and arguments from the JSON structure
        toolCalls = data.get('message', {}).get('toolCalls', [])
        result = []
        ordetTotal = 0
        # print('toolCalls ::', toolCalls)
        for toolCall in toolCalls:
            toolCallId = toolCall.get('id', 'unknown')
            arguments = toolCall.get('function', {}).get('arguments', {})
            order = arguments.get('order', [])

            if order is not None:
                print('Before ordetTotal ::', ordetTotal)
                ordetTotal += getTotal(order)
                print('After ordetTotal ::', ordetTotal)
                
                result.append(
                    {
                    "toolCallId": toolCallId,
                    "result": f"Order Total : {ordetTotal}"
                }
                )
                
                
            else:
                return jsonify({"error": "Order is missing in the request"}), 400
        
        response_json = {"results": result}
        print('response_json::', response_json)
        print('Resonse to return ::', jsonify(response_json))


        # emit the current order event
        emit_current_order_event()

        # calling the function to save the order
        # todo:: call this function in the separate thread as it is independent of this flow
        # save_order_to_db(ordetTotal)


        # saving the order details to global state
        print('Total to add to the global state ::', ordetTotal)
        global_order['total'] = ordetTotal
        global_order['orderDate'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return jsonify(response_json)

    else:
        return jsonify({"error": "Request should be in JSON format"}), 400
    