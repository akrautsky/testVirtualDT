import firebase_admin
from firebase_admin import credentials, firestore


def initFirebase(app):
    # setup the creds
    cred = credentials.Certificate("app/firebaseCreds.json")
    firebase_admin.initialize_app(cred)

    #initialize the app
    app.firebase_db = firestore.client()


