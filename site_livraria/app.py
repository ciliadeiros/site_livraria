from flask import Flask, render_template , request, redirect, url_for, session, make_response, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from modelos import User
import sqlite3 
from database import obter_conexao

login_manager = LoginManager() 
app = Flask(__name__)
app.secret_key = 'ablublublu'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

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
        print(f'Email: {email}, Nome {nome}, Senha:{senha}, Preferencias:{preferencias}')

        conexao = obter_conexao()
        sql = "SELECT * FROM usuarios WHERE usu_email = ?"
        resultado = conexao.execute(sql, (email,) ).fetchone()
        
        if not resultado:
            sql = "INSERT INTO usuarios(usu_email, usu_nome, usu_senha, usu_preferencias) VALUES(?,?,?,?)"
            conexao.execute(sql, (email, nome, senha, preferencias))
            conexao.commit()
            conexao.close()

            # login do usuário
            user = User(email=email, nome=nome, senha=senha)
            user.id = email
            login_user(user)

            flash('Cadastro realizado com sucesso', category='success')
            return redirect(url_for('index'))

        else:
            flash('E-mail já cadastrado. Tente outro.', category='error')
            conexao.close()

    return render_template('cadastro.html')

@app.route('/login')
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # conectar com o banco de dados
        conexao = obter_conexao()
        sql = "SELECT * FROM users WHERE email = ? AND senha = ?"
        resultado = conexao.execute(sql, (email, senha)).fetchone()
        conexao.close()

        if resultado:
            user = User(email=email, nome=nome, senha=senha)
            user.id = email
            login_user(user)
            flash('Login feito com sucesso!', category='success')
            return redirect(url_for('dash'))
        
        else:
            flash('Usuário ou senha incorretos. Tente novamente.', category='error')
            return redirect(url_for('login'))

    return render_template('login.html')

@login_required
@app.route('/livros')
def livros():
    return render_template('livros.html')

@login_required
@app.route('/biblioteca')
def biblioteca():
    return render_template('biblioteca.html')

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login")) 

# Rodar o app
if __name__ == '__main__':
    app.run(debug=True)