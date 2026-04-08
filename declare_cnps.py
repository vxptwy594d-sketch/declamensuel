import pyodbc

# Connection string for SQL Server
connection_string = (
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=your_server_name;'
    'Database=your_database_name;'
    'UID=your_username;'
    'PWD=your_password;'
)

try:
    # Establish connection
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    # Example query
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    cursor.close()
    conn.close()
    
except Exception 
 print(f"Connection error: {e}")