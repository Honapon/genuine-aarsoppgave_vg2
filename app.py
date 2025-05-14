from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logInn.html')
def logInn():
        return render_template('logInn.html')


if __name__ == '__main__':
    app.run(debug=True)
    