import sqlite3

# Connect to the database file
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a test SQL statement to check if the database exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

# If the database doesn't exist, create a new table
if not cursor.fetchall():
    cursor.execute("CREATE TABLE mytable (id INTEGER PRIMARY KEY, name TEXT)")

# Commit the changes and close the connection
conn.commit()
conn.close()