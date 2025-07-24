from flask import Flask, render_template , request, redirect, url_for, session, make_response, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from modelos import User
import sqlite3 
from database import obter_conexao
from flask import session, redirect
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
    # #cria o dicionario para guardar os dados
    # if 'usuarios' not in session:
    #     usuarios = {}
    #     session['usuarios'] = usuarios
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        email = request.form['email']
        nome = request.form['nome']
        senha = request.form['senha']
        preferencias = request.form['preferencias']
        print(f'Email: {email}, Nome {nome}, Senha:{senha}, Preferencias:{preferencias}')
        senha_criptografada = generate_password_hash(senha)

        conexao = obter_conexao()
        sql = "SELECT * FROM usuarios WHERE usu_email = ?"
        resultado = conexao.execute(sql, (email,) ).fetchone()
        
        if not resultado:
            sql = "INSERT INTO usuarios(usu_email, usu_nome, usu_senha, usu_preferencias) VALUES(?,?,?,?)"
            conexao.execute(sql, (email, nome, senha_criptografada, preferencias))
            conexao.commit()
            conexao.close()

            # login do usuário
            user = User(email=email, nome=nome, senha=senha_criptografada)
            user.id = email
            login_user(user)

            flash('Cadastro realizado com sucesso', category='success')
            return redirect(url_for('index'))

        else:
            flash('E-mail já cadastrado. Tente outro.', category='error')
            conexao.close()

    return render_template('cadastro.html')

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        #recebe os dados do usuário no formuário
        email = request.form['email']
        senha = request.form['senha']

        conexao = sqlite3.connect('banco.db') #conecta ao banco de dados
        conexao.row_factory = sqlite3.Row #as informações vem em formato de dicionários
        sql = "SELECT * FROM users WHERE email = ? AND senha = ?"  # procura o usuário que possui esses dados
        resultado  = conexao.execute(sql, (email, senha)).fetchone() # retorna o usuário
        conexao.close() # a conexão com o banco de dados é encerrada
        if resultado: # se o usuário foi encontrado e retornado...
            # user = User(email=email, senha=senha) # 'user' é a tabela do banco, e 'senha' e 'email' os valores. essa função cria um novo usuário
            user = User(id= resultado['id'], email= resultado['email'], senha = resultado['senha']) # confere os dados do usuário, o id é inserido automaticamente no banco de dados
            login_user(user) # o usuário é logado
            flash('Login feito com sucesso!', category='success')
            return redirect(url_for('livros')) # retorna                                                                                                                                  
    return render_template('login.html')
        #     return redirect(url_for('login'))
    # if request.method == 'POST':
    #     email = request.form['email']
    #     senha = request.form['senha']

    #     dicionario = session.get('usuarios')
    #     #realiza o login do usuário
    #     if email in dicionario and senha == dicionario[senha]:
    #         utilizador= User(nome=email,senha=senha)
    #         print('Dicionário:', dicionario)
    #         utilizador.id = email
    #         login_user(utilizador)
    #         return redirect(url_for('livros')) # reireciona para a pagina os livros
    #     #se você não está logado ou digitou senha/email errado, vai aparecer essa mensagem de erro
    #     flash ('Senha ou login incorreto',category='error')
    #     return redirect (url_for('login'))

    # return render_template('login.html')
        # # conectar com o banco de dados
        # conexao = obter_conexao()
        # sql = "SELECT * FROM users WHERE email = ? AND senha = ?"
        # resultado = conexao.execute(sql, (email, senha)).fetchone()
        # conexao.close()

        # if resultado:
        #     user = User(email=email, nome=nome, senha=senha)
        #     user.id = email
        #     login_user(user)
        #     flash('Login feito com sucesso!', category='success')
        #     return redirect(url_for('dash'))
        
        # else:
        #     flash('Usuário ou senha incorretos. Tente novamente.', category='error')
        #     return redirect(url_for('login'))


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