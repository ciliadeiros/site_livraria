DROP TABLE IF EXISTS usuarios;

CREATE TABLE IF NOT EXISTS usuarios (
    usu_email TEXT PRIMARY KEY NOT NULL,
    --cadastra o email do usuario como chave de identificação que não pode ficar em branco
    usu_senha TEXT NOT NULL,
    --senha também não pode ficar em branco, será harsh
    usu_preferencias TEXT,
    usu_nome TEXT NOT NULL
);

DROP TABLE IF EXISTS livros;

CREATE TABLE IF NOT EXISTS livros (
    liv_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    liv_autor TEXT NOT NULL,
    liv_titulo TEXT NOT NULL
);