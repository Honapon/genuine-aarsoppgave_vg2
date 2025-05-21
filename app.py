from flask import Flask, render_template, request, redirect, url_for, session, flash
from bcrypt import hashpw, gensalt, checkpw
from data import dbconnect
import re



app = Flask(__name__)
app.secret_key = 'your_secret_key'  


    
@app.route('/createAcc', methods=['POST', 'GET'])

        
def createAccc():
    if request.method == 'POST':
        
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not username or not email or not password:
            flash('All fields are required', 'error')
            return render_template('createAcc.html')
        
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            flash('E-postadressen er ikke gyldig', 'error')
            return render_template('createAcc.html')
        
        if email_exists(email):
            flash('Email already exists', 'error')
            return render_template('createAcc.html')

        hashed_password = hashpw(password.encode('utf-8'), gensalt())

        if create_user(username, email, hashed_password):
            flash('User created successfully')
            return redirect(url_for('logInn'))
        else:
            flash('Error creating user', 'error')
            
        if not all([username, email, password]):
            return('All fields are required', 'error')
            
            
    return render_template('createAcc.html')
        
@app.route('/login', methods=['POST', 'GET'])
def logInn():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if authenticate_user(email, password):
            session['email'] = email
            flash('You have been logged in')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
            return render_template('logInn.html')
    return render_template('logInn.html')    

@app.route('/hjem')
def home():
    if 'email' in session:
        return render_template('hjem.html', email=session['email'])
    else:
        flash('You need to log in first', 'error')
        return redirect(url_for('logInn'))
            
@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You have been logged out')
    return redirect(url_for('index'))            

@app.route('/')
def index():
    return render_template('index.html')
    

def authenticate_user(email, password):
    connection = dbconnect()
    if connection is None:
        flash('Database connection error', 'error')
        return False

    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM brukere WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        if user and checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return True
        else:
            return False   
    except Exception as e:
        flash(f"Error executing query: {e}", 'error')
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_user(username, email, hashed_password):
    connection = dbconnect()
    if connection is None:
        flash('Database connection error', 'error')
        return False
    try:
        cursor = connection.cursor()
        query = "INSERT INTO brukere (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, hashed_password))
        connection.commit()
        return True
    except Exception as e:
        if 'Duplicate entry' in str(e):
            flash('Email already exists', 'error')
            return False
        else:
            flash(f"database error: {e}", 'error')
            return False
    finally: 
        if connection.is_connected():
            cursor.close()
            connection.close()
            
            
def email_exists(email):
    connection = dbconnect()
    if connection is None:
        return False
    try:
        cursor = connection.cursor()
        query = "SELECT id FROM brukere WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result is not None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
if __name__ == '__main__':
    app.run(debug=True)