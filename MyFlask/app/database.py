from flask_sqlalchemy import SQLAlchemy


#create the instance to sqlAlchemy
db = SQLAlchemy()

def init_db(app):
    # Configuration setup
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Akashr%4007@localhost:3306/VDOrderDB'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    