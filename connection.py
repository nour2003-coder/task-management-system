import pyodbc
def connect_to_db():
    try:
        
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'  
            'SERVER=localhost;'  
            'DATABASE=rita_project;'  
            'Trusted_Connection=yes;'  
        )
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
    return connection
