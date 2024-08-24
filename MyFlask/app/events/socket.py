from flask_socketio import SocketIO

# Initialize SocketIO but do not pass the app here
socketIO = SocketIO(cors_allowed_origins=["http://localhost:3000"])
