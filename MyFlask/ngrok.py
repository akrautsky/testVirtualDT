# ngrok.py
from pyngrok import ngrok
import os
from app import create_app
from app.events.current_order_event import socketIO

# Specify the port on which your Flask app is running
port = 5000

# Start an ngrok tunnel
public_url = ngrok.connect(port)
print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

# Create the Flask app
app = create_app()


    
@socketIO.on('connect')
def handle_connect():
    print('Client connected')

# Now, run your Flask app using SocketIO and specify the port
if __name__ == '__main__':
    socketIO.run(app, port=port)
