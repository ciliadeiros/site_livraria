from flask_login import UserMixin
from database import obter_conexao

class User(UserMixin):
    def __init__(self, email, nome, senha):
        self.id = email  # Flask-Login usa "id" como identificador (nesse caso, será o e-mail)
        self.email = email
        self.nome = nome
        self.senha = senha

    # procura um usuário no banco pelo e-mail (usu_email), que é o ID
    @classmethod
    def get(cls, user_id):
        conexao = obter_conexao()
        sql = "SELECT * FROM usuarios WHERE usu_email = ?"
        resultado = conexao.execute(sql, (user_id,)).fetchone()

        if resultado:
            return User(
                email=resultado['usu_email'],
                nome=resultado['usu_nome'],
                senha=resultado['usu_senha']
            )
        return None

    @classmethod
    def find_email(cls, email):
        conexao = obter_conexao()
        sql = "SELECT * FROM usuarios WHERE usu_email = ?"
        resultado = conexao.execute(sql, (email,)).fetchone()

        if resultado:
            return User(
                email=resultado['usu_email'],
                nome=resultado['usu_nome'],
                senha=resultado['usu_senha']
            )
        return None

    # salva o usuário no banco de dados
    def save(self):
        conexao = obter_conexao()
        sql = """
            INSERT INTO usuarios (usu_email, usu_nome, usu_senha)
            VALUES (?, ?, ?)
        """
        conexao.execute(sql, (self.email, self.nome, self.senha))
        conexao.commit()

    # apaga o usuário do banco de dados
    @classmethod
    def delete(cls, email):
        conexao = obter_conexao()
        sql = "DELETE FROM usuarios WHERE usu_email = ?"
        conexao.execute(sql, (email,))
        conexao.commit()
