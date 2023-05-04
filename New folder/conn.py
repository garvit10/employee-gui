import mysql.connector

# set up the connection parameters
config = {
    'user': 'root',
    'password': 'piyush007Q#!',
    'host': 'localhost',
    'database': 'emoloyeedb'
}

# create the connection
cnx = mysql.connector.connect(**config)

# check the connection
if cnx.is_connected():
    print('Connection successful!')
else:
    print('Connection failed.')
    
# close the connection
cnx.close()
