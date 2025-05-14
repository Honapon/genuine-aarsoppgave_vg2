from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

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
    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logInn.html')
def logInn():
        return render_template('logInn.html')
    
@app.route('/createAcc.html')
def create():
    return render_template('createAcc.html')



if __name__ == '__main__':
    app.run(debug=True)
    