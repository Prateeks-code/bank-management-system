from flask import Flask, render_template, request, redirect, session
from config import get_db_connection

app = Flask(__name__)
app.secret_key = "secret123"  # for sessions

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Register
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)", (name,email,password))
        conn.commit()
        conn.close()
        return redirect('/login')
    return render_template('register.html')

# Login
@app.route('/login', methods=['GET','POST'])

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email,password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            session['name'] = user['name']
            return redirect('/dashboard')
    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT balance FROM users WHERE id=%s", (session['user_id'],))
    balance = cursor.fetchone()['balance']
    conn.close()

    return render_template('dashboard.html', name=session['name'], balance=balance)

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
