import mysql.connector

try:
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",          
        user="root",      
        password="Nour21644162-",  
        database="rita_project"    
    )

    # Check if the connection is successful
    if connection.is_connected():
        print("Connected to the database")


except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")