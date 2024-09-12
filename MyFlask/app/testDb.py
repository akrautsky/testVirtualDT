from sqlalchemy import create_engine, text

# Connection string with the provided credentials
DATABASE_URL = (
    "mssql+pyodbc://admin07:Akashr%4007@vdsqldbserver.database.windows.net:1433/VDTDB"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&Encrypt=yes"
    "&TrustServerCertificate=no"
    "&Connection Timeout=30"
)

# Create an engine instance
engine = create_engine(DATABASE_URL, echo=True)

# Test the connection by executing a simple query
try:
    with engine.connect() as connection:
        # Use text() to execute a raw SQL query
        result = connection.execute(text("SELECT @@version;"))
        for row in result:
            print(row)
except Exception as e:
    print(f"An error occurred: {e}")
