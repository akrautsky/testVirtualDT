from flask import Flask
from flask_cors import CORS
from app.database import init_db
from app.firebaseDB import initFirebase
from flask_socketio import SocketIO
from app.events.socket import socketIO


def create_app():
    app = Flask(__name__)


    # specifying the allowed origins
    cors = CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000"]}})
    
    # initializing the socketIO with app
    socketIO.init_app(app)

    # initializing the SQL database
    init_db(app)

    # initializing the firebase database
    initFirebase(app)


    # registering the blueprints with app
    from .routes import register_blueprint
    register_blueprint(app)
    return app