-- DROP TABLE IF EXISTS usuarios;

CREATE TABLE IF NOT EXISTS usuarios (
    usu_email TEXT PRIMARY KEY NOT NULL,
    --cadastra o email do usuario como chave de identificação que não pode ficar em branco
    usu_senha TEXT NOT NULL,
    --senha também não pode ficar em branco, será harsh
    usu_preferencias TEXT,
    usu_nome TEXT NOT NULL
);

--DROP TABLE IF EXISTS livros;

CREATE TABLE IF NOT EXISTS livros (
    liv_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    liv_autor TEXT NOT NULL,
    liv_titulo TEXT NOT NULL,
    liv_genero TEXT NOT NULL,
    liv_lancamento DATE NOT NULL,
    liv_editora TEXT NOT NULL,
    liv_descricao TEXT NOT NULL,
    liv_pags INTEGER NOT NULL,
    liv_capa TEXT NOT NULL
);

--DROP TABLE IF EXISTS usuarios_livros;

-- Tabela de ligação muitos-para-muitos
CREATE TABLE IF NOT EXISTS usuarios_livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usu_email TEXT NOT NULL,
    liv_id INTEGER NOT NULL,
    FOREIGN KEY (usu_email) REFERENCES usuarios(usu_email),
    FOREIGN KEY (liv_id) REFERENCES livros(liv_id)
);