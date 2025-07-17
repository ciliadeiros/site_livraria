import sqlite3

def obter_conexao():
    ''' Cria uma conexão com o arquivo de banco de dados banco.db.
        Se o arquivo não existir, ele será criado automaticamente. '''
    conexao = sqlite3.connect('banco.db')
    conexao.row_factory = sqlite3.Row
    return conexao