from app import create_app
from flask_cors import CORS
from app.events.current_order_event import socketIO

app = create_app()




if __name__ == '__main__':
    socketIO.run(app, debug=True)