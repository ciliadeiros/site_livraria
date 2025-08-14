from flask import Flask, render_template , request, redirect, url_for, session, make_response, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from modelos import User
import sqlite3 
from database import obter_conexao
from flask import session, redirect
login_manager = LoginManager()
login_manager.login_view = 'login'
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

            return redirect(url_for('index'))

        else:
            flash('E-mail já cadastrado. Tente outro.', category='error')
            conexao.close()

    return render_template('cadastro.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        conexao = obter_conexao()
        conexao.row_factory = sqlite3.Row
        sql = "SELECT * FROM usuarios WHERE usu_email = ?"
        resultado = conexao.execute(sql, (email,)).fetchone()
        conexao.close()

        if resultado and check_password_hash(resultado['usu_senha'], senha):
            user = User(
                email=resultado['usu_email'],
                nome=resultado['usu_nome'],
                senha=resultado['usu_senha']
            )
            login_user(user)
            flash('Login feito com sucesso!', category='success')
            return redirect(url_for('livros'))
        else:
            flash('Usuário ou senha incorretos. Tente novamente :/', category='error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/perfil')
@login_required
def perfil():
    conexao = obter_conexao()
    conexao.row_factory = sqlite3.Row

    sql = "SELECT usu_email, usu_nome, usu_preferencias FROM usuarios WHERE usu_email = ?"
    resultado = conexao.execute(sql, (current_user.email,)).fetchone()
    conexao.close()

    if resultado:
        usu_info = {
            'nome': resultado['usu_nome'],
            'email': resultado['usu_email'],
            'preferencias': resultado['usu_preferencias']
        }
        return render_template('perfil.html', usuario=usu_info)
    
    return redirect(url_for('cadastro'))

@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    conexao = obter_conexao()
    conexao.row_factory = sqlite3.Row

    if request.method == 'POST':
        novo_nome = request.form['nome']
        novo_email = request.form['email']
        novas_pref = request.form['preferencias']

        conexao.execute("""
            UPDATE usuarios
            SET usu_nome = ?, usu_email = ?, usu_preferencias = ?
            WHERE usu_email = ?
        """, (novo_nome, novo_email, novas_pref, current_user.email))
        conexao.commit()
        conexao.close()

        current_user.email = novo_email  # Atualiza o email da sessão
        flash('Perfil atualizado com sucesso!', 'success')
        return redirect(url_for('perfil'))

    resultado = conexao.execute("""
        SELECT usu_email, usu_nome, usu_preferencias
        FROM usuarios
        WHERE usu_email = ?
    """, (current_user.email,)).fetchone()
    conexao.close()

    if resultado:
        usuario = {
            'nome': resultado['usu_nome'],
            'email': resultado['usu_email'],
            'preferencias': resultado['usu_preferencias']
        }
        return render_template('editar_perfil.html', usuario=usuario)

    return redirect(url_for('perfil'))


@app.route('/biblioteca', methods=["GET", "POST"])
@login_required
def biblioteca():
    email_usuario = current_user.email
    conexao = obter_conexao()
    conexao.row_factory = sqlite3.Row
    SQL = "SELECT * FROM livros JOIN usuarios_livros ON livros.liv_id = usuarios_livros.liv_id WHERE usuarios_livros.usu_email = ?"
    books_biblioteca = conexao.execute(SQL, (email_usuario,)).fetchall()
    conexao.close()
    return render_template('biblioteca.html', books_biblioteca=books_biblioteca)

@app.route("/adicionar_livro", methods=["GET", "POST"])
@login_required
def adicionar_livro():
    liv_id = request.form.get("liv_id")
    usu_email = current_user.id

    conexao = obter_conexao()
    conexao.row_factory = sqlite3.Row

    # Verifica se o livro existe
    livro = conexao.execute("SELECT liv_id FROM livros WHERE liv_id = ?", (liv_id,)).fetchone()

    if livro:
        # Verifica se já está adicionado
        existe = conexao.execute(
            "SELECT usuarios_livros.liv_id FROM usuarios_livros WHERE usu_email = ? AND liv_id = ?",
            (usu_email, liv_id)
        ).fetchone()

        if not existe:
            conexao.execute(
                "INSERT INTO usuarios_livros (usu_email, liv_id) VALUES (?, ?)",
                (usu_email, liv_id)
            )
            conexao.commit()

    conexao.close()
    return redirect(url_for("livros"))

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login")) 

@login_required
@app.route('/livros')
def livros():
    conexao = obter_conexao()
    conexao.row_factory = sqlite3.Row
    SQL = "SELECT * FROM livros"
    livros = conexao.execute(SQL).fetchall()
    conexao.close()
    return render_template('livros.html', livros=livros)

@app.route('/livros/<int:livro_id>')
def detalhar_livro(livro_id):
    conexao = obter_conexao()
    conexao.row_factory = sqlite3.Row
    livro = conexao.execute('SELECT * FROM livros WHERE liv_id = ?', (livro_id,)).fetchone()
    conexao.close()
    # if livro is None:
    #     return "Livro não encontrado", 404
    return render_template('detalhe_livro.html', livro=livro)

@app.route('/retirar_livro', methods=['POST'])
@login_required
def retirar_livro():
    liv_id = request.form['liv_id']
    usu_email = current_user.id

    conexao = obter_conexao()
    SQL = "DELETE FROM usuarios_livros WHERE usu_email = ? AND liv_id = ?"
    conexao.execute(SQL, (usu_email, liv_id))
    conexao.commit()
    conexao.close()
    return redirect(url_for('biblioteca'))

# Rodar o app
if __name__ == '__main__':
    app.run(debug=True)
