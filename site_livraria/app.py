from flask import Flask, render_template , request, redirect, url_for, session, make_response, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
import sqlite3
#cria o app
app = Flask(__name__)

def obter_conexao():
    ''' Cria uma conexão com o arquivo de banco de dados banco.db.
        Se o arquivo não existir, ele será criado automaticamente. '''
    conexao = sqlite3.connect('banco.db')
    conexao.row_factory = sqlite3.Row
    return conexao

@login_required
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        email = request.form['email']
        nome = request.form['nome']
        senha = request.form['senha']
        preferencias = request.form['preferencias']

    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@login_required
@app.route('/livros')
def livros():
    return render_template('livros.html')

@login_required
@app.route('/biblioteca')
def biblioteca():
    return render_template('biblioteca.html')

# Rodar o app
if __name__ == '__main__':
    app.run(debug=True)
