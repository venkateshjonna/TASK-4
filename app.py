from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

users = {}

@app.route('/')
def index():
    if 'username' in session:
        return render_template('secure.html', username=session['username'])
    return render_template('main.html')
    # return 'You are not logged in. <br><a href="/login">Login</a> <br><a href="/register">Register</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Incorrect username or password!'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return 'Username already exists!'
        else:
            users[username] = password
            return 'Registered successfully!<br> <button><a href="/login">Login</a></button>'

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
