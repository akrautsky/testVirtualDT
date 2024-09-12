from flask_sqlalchemy import SQLAlchemy


#create the instance to sqlAlchemy
db = SQLAlchemy()

def init_db(app):
    # Configuration setup

    # Azure SQL Database connection string
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        "mssql+pyodbc://admin07:Akashr%4007@vdsqldbserver.database.windows.net:1433/VDTDB"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&Encrypt=yes"
        "&TrustServerCertificate=no"
        "&Connection Timeout=30"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database with the app
    try:
        db.init_app(app)
        print("Database connection initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize the database connection: {e}")

