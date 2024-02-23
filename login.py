from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'random_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'ivan' and request.form['password'] == 'faki':
            session['userID'] = request.form['username']
            return redirect(url_for('profil'))
        return render_template('login.html', unsuccess=True)
    return render_template('login.html', unsuccess=False)


@app.route('/logout')
def logout():
    if 'userID' in session:
        session.pop('userID', None)
    return redirect(url_for('profil'))


@app.route('/profil')
def profil():
    return render_template('profil.html')


if __name__ == '__main__':
    app.run(port=5001)
