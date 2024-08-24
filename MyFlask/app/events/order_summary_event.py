from flask_socketio import  emit
from app.globals.global_states import global_order
from app.events.socket import socketIO



def emit_order_summary_event():
    # allowing all the origins to connect to the socket for time being
    print('Emiting the event::', {"items":global_order})
    socketIO.emit('order_summary', {"items":global_order})
    


