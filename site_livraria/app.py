from flask import Flask, render_template #, request, redirect, url_for, session, make_response, flash
# from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
#cria o app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def index():
    return render_template('cadastro.html')

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/livros')
def index():
    return render_template('livros.html')

@app.route('/biblioteca')
def index():
    return render_template('biblioteca.html')

# Rodar o app
if __name__ == '__main__':
    app.run(debug=True)
