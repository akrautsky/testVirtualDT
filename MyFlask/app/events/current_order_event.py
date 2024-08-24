from flask_socketio import SocketIO, emit
from app.globals.global_states import global_order
from app.globals.global_states import global_order_items
from app.events.socket import socketIO



def emit_current_order_event():
    # allowing all the origins to connect to the socket for time being
    print('Emiting the event::', {"items":global_order_items})
    socketIO.emit('current_order', {"items":global_order_items})
    


