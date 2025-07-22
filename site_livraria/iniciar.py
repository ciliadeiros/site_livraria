import sqlite3

BANCO='schemas.sql'

# conectar com o banco
conexao = sqlite3.connect('site_livrariabanco.db')

# executar a criação tabela
with open(BANCO) as f:
    conexao.executescript(f.read())

conexao.close()
# fechar conexao

