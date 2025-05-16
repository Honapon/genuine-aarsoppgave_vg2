import mysql.connector
from mysql.connector import Error

mydb = {
    'host': '172.28.110.89',
    'user': 'stiimDb',
    'password': 'steamkopi',
    'database': 'stiim'
}



# Funksjon for å opprette en tilkobling til databasen
def dbconnect():
    try:
        connection = mysql.connector.connect(**mydb)
        return connection
        
    except Error as e:
        print(f"Error connecting to mariadb: {e}")
        return None
    