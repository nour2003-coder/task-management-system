import pyodbc
def connect_to_db():
    try:
        # Establish a connection to SQL Server using Windows Authentication
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'  # Change driver if needed
            'SERVER=localhost;'  # Your SQL Server instance
            'DATABASE=rita_project;'  # Database name
            'Trusted_Connection=yes;'  # Windows Authentication (no need for username and password)
        )
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
    return connection
