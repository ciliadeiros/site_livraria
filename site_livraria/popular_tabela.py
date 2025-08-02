import sqlite3

conn = sqlite3.connect('site_livrariabanco.db')
conn.row_factory = sqlite3.Row

books = [
    (
        'J. K. Rowling',
        'Harry Potter e a Pedra Filosofal',
        'Romance e Fantasia',
        '1997-01-01',
        'Rocco',
        'Harry Potter é um garoto cujos pais, feiticeiros, foram assassinados por um poderosíssimo bruxo quando ele ainda era um bebê. Ele foi levado, então, para a casa dos tios que nada tinham a ver com o sobrenatural. Pelo contrário. Até os 10 anos, Harry foi uma espécie de gata borralheira: maltratado pelos tios, herdava roupas velhas do primo gorducho, tinha óculos remendados e era tratado como um estorvo. No dia de seu aniversário de 11 anos, entretanto, ele parece deslizar por um buraco sem fundo, como o de Alice no país das maravilhas, que o conduz a um mundo mágico. Descobre sua verdadeira história e seu destino: ser um aprendiz de feiticeiro até o dia em que terá que enfrentar a pior força do mal, o homem que assassinou seus pais. O menino de olhos verde, magricela e desengonçado, tão habituado à rejeição, descobre, também, que é um herói no universo dos magos. Potter fica sabendo que é a única pessoa a ter sobrevivido a um ataque do tal bruxo do mal e essa é a causa da marca em forma de raio que ele carrega na testa. Ele não é um garoto qualquer, ele sequer é um feiticeiro qualquer ele é Harry Potter, símbolo de poder, resistência e um líder natural entre os sobrenaturais. A fábula, recheada de fantasmas, paredes que falam, caldeirões, sapos, unicórnios, dragões e gigantes, não é, entretanto, apenas um passatempo.',
        208,
        'https://m.media-amazon.com/images/I/51p3o+A5GOL._UF1000,1000_QL80_.jpg'
    ),
    (
        'Lewis Carroll',
        'Alice no País das Maravilhas',
        'Fantasia e Literatura Nonsense',
        '1865-07-04',
        'Darkside',
        'Uma menina, um coelho e uma história capazes de fazer qualquer um de nós voltar a sonhar. Alice é despertada de um leve sono ao pé de uma árvore por um coelho peculiar. Uma criatura alva e falante com roupas engraçadas, que consulta seu relógio e reclama do próprio atraso. Curiosa como toda criança, Alice segue o animal até cair em um buraco sem fim que mudou para sempre a literatura infantil. Mais de 150 anos depois, Alice no País das Maravilhas continua repleto de ensinamentos para aqueles que ousaram seguir o Coelho Branco até sua toca.',
        208,
        'https://darkside.vtexassets.com/arquivos/ids/198445/239-alice-classic-edition-0.jpg?v=638742941929970000'
    ),
    (
        'Jenna Evans Welch',
        'Amor e Gelato',
        'Romance',
        '2017-07-21',
        'Intrínseca',
        'Um verão na Itália, uma antiga história de amor e um segredo de família. Depois da morte da mãe, Lina fica com a missão de realizar um último pedido: ir até a Itália para conhecer o pai. Do dia para a noite, ela se vê na famosa paisagem da Toscana, morando em uma casa localizada no mesmo terreno de um cemitério memorial de soldados americanos da Segunda Guerra Mundial, com um homem que nunca tinha ouvido falar. Apesar das belezas arquitetônicas, da história da cidade e das comidas maravilhosas, o que Lina mais quer é ir embora correndo dali. Mas as coisas começam a mudar quando ela recebe um antigo diário da mãe. Nele, a menina embarca em uma misteriosa história de amor, que pode explicar suas próprias origens. No meio desse turbilhão de emoções, Lina ainda conhece Ren e Thomas, dois meninos lindos que vão mexer ainda mais com seu coração. Uma trajetória que fará Lina descobrir o amor, a si mesma e também aprender a lidar com a perda. Amor & gelato é uma deliciosa viagem pelos mais românticos pontos turísticos italianos, com direito a tudo de mais intenso que o lugar tem a oferecer: desde paixões até corações partidos.',
        320,
        'https://m.media-amazon.com/images/I/81EE1CAUoEL.jpg'
    ),
    (
        'Ludmila B. Teixeira',
        'A Canção dos Etéreos: Starcrossed',
        'Romance Medieval, Fantasia e Drama',
        '2023-01-14',
        '(Autopublicação)',
        'Quando Iwan Morgan, príncipe-herdeiro de Camlet, abandona sua noiva prometida em um casamento político para desposar outra mulher, o equilíbrio entre os Seis Reinos de Untria desmorona. Meio a essa turbulência, a princesa Awena, irmã de Iwan, tenta se preparar para os árduos testes da Academia de Ciallmhar, onde ela poderá seguir com seu sonho de estudar as artes médicas. Porém, um dilema a atormenta: caso ela seja aprovada, precisará deixar o reino, e como abandonar sua família justo agora com uma guerra iminente e com a vida de seu irmão por um fio? Enquanto isso, a família Morgan, temendo que Awena esteja correndo perigo, contrata um guerreiro vindo das distantes Agulhas de Gelo como seu guardião. Bonito, misterioso e rabugento na mesma medida, Valin começa a mexer com os sentimentos de Awena, deixando-a completamente confusa. O guerreiro, por sua vez, acaba descobrindo que todo o seu treinamento não o havia preparado para a maior provação de todas: tornar-se guarda da princesa mais obstinada e temperamental de todo o Grande Reino de Untria. Entre honra, lealdade, paixão e um romance tão arrebatador que desafia os desígnios dos Etéreos, cada escolha trará um sacrifício a ser feito.',
        422,
        'https://m.media-amazon.com/images/I/81QPj8fFEHL._UF894,1000_QL80_.jpg'
    ),
    (
        'Gerald Brittle, Ed Warren & Lorraine Warren',
        'Ed & Lorraine Warren: Demonologistas – Arquivos Sobrenaturais',
        'Não Ficção, Sobrenatural, Terror e Suspense',
        '2016-01-01',
        'DarkSide Books',
        'Em ED & LORRAINE WARREN: DEMONOLOGISTAS, Gerald Brittle desvenda alguns dos principais casos reais vividos pelos Warren. Ed e Lorraine permitiram ao autor acesso exclusivo aos seus arquivos sobrenaturais, que incluem relatos extraordinários de poltergeists, casas mal-assombradas e possessões demoníacas. O resultado é um livro rico em detalhes como nenhum outro. Lançado originalmente em 1980, e até então inédito no Brasil, ED & LORRAINE WARREN: DEMONOLOGISTAS é, sem dúvida, o mais completo dossiê sobre os exorcistas/caçadores de fantasmas mais famosos do mundo. Virou o livro de cabeceira do diretor James Wan (Jogos Mortais, Invocação do Mal 1 e 2, Annabelle), além de servir de fonte de inspiração para Vera Farmiga, que interpreta a Sra. Warren no cinema.',
        272,
        'https://m.media-amazon.com/images/I/91Cu2hkpMlL._UF894,1000_QL80_.jpg'
    ),
    (
        'Ed Warren, Lorraine Warren, Carmen Reed, Al Snedeker & Ray Garton',
        'Ed & Lorraine Warren: Lugar Sombrio',
        'Não Ficção, Sobrenatural, Terror e Suspense',
        '2018-02-28',
        'DarkSide Books',
        'ED & LORRAINE WARREN: LUGAR SOMBRIO, é o relato meticuloso dos fenômenos que infernizaram a vida de um casal norte-americano após sua mudança para uma antiga casa em que havia funcionado uma funerária anos antes. Um a um, os membros da família passam a ser atacados por uma presença sinistra, em acontecimentos cada vez mais extremos: de vozes na escuridão até violações fantasmas. É nesse ambiente de desespero queEd & Lorraine Warren são recebidos, prontos para mais um combate direto com o mundo das sombras. O exorcismo de Connecticut ganhou notoriedade na mídia norte-americana na época. Em 2009, a história serviu de inspiração para o filme Evocando Espíritos, de Peter Cornwell, que usou Ed & Lorraine Warren: Lugar Sombrio como principal fonte de pesquisa.',
        272,
        'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjil41fa9-QHzCn7ocUhcEBpQ6CO85RXW_BSGABJ3RvNcWg1vDaHUUwNRI9GQUYcrWQKC6vU9pyhPWvflF1KhcFAAGiceUuGLBxO9h7nEDHATXwRS8RgEXjtISWVFCwW_zo1wowu41LI2F3pYpoV5LXknkSBLK14zpLND6Pu-jo17Le7rkql2wKkAyMpA/s600/LugarSombrio.jpg'
    ),
    (
        'Suzanne Collins',
        'Jogos Vorazes',
        'Distopia, Aventura, Ficcção Científica, Romance',
        '2010-05-29',
        'Rocco',
        'Após o fim da América do Norte, uma nova nação chamada Panem surge. Formada por doze distritos, é comandada com mão de ferro pela Capital. Uma das formas com que demonstra seu poder sobre o resto do carente país é com Jogos Vorazes, uma competição anual transmitida ao vivo pela televisão, em que um garoto e uma garota de doze a dezoito anos de cada distrito são selecionados e obrigados a lutar até a morte! Para evitar que sua irmã seja a mais nova vítima do programa, Katniss se oferece para participar em seu lugar. Vinda do empobrecido Distrito 12, ela sabe como sobreviver em um ambiente hostil. Peeta, um garoto que ajudou sua família no passado, também foi selecionado. Caso vença, terá fama e fortuna. Se perder, morre. Mas para ganhar a competição, será preciso muito mais do que habilidade. Até onde Katniss estará disposta a ir para ser vitoriosa nos Jogos Vorazes?',
        400,
        'https://static.skeelo.com/resize/1024/2048/80/1083/9786555952360.jpg'
    ),
    (
        'James Dashner',
        'Maze Runner: Correr ou Morrer',
        'Ficção Científica, Ação, Distopia',
        '2010-07-28',
        'Plataforma 21',
        'Sua vida anterior já não existe mais. Uma nova se inicia. Lembre. Corra. Sobreviva. Ao acordar dentro de um escuro elevador em movimento. a única coisa que Thomas consegue lembrar é de seu nome. Sua memória está completamente apagada. Mas ele não está soz.',
        428,
        'https://m.media-amazon.com/images/I/81UuGTd7RuL._UF1000,1000_QL80_.jpg'
    ),
    (
        'Jeff Kinney',
        'Diário de um Banana 1',
        'Comédia, Infantil',
        '2008-05-19',
        'VR Editora',
        'Não é fácil ser criança. E ninguém sabe disso melhor do que Greg Heffley, que se vê mergulhado no mundo do ensino fundamental, onde fracotes são obrigados a dividir os corredores com garotos mais altos, mais malvados e que já se barbeiam. Em Diário de um Banana, o autor e ilustrados Jeff Kinney nos apresenta um herói improvável. Como Greg diz em seu diário. Só não espere que seja todo Querido Diário isso, Querido Diário aquilo. Para nossa sorte, o que Greg Heffley diz que fará e o que ele realmente faz são duas coisas bem diferentes.',
        224,
        'https://m.media-amazon.com/images/I/71fWaI5myqL._UF1000,1000_QL80_.jpg'
    )
]

sql = """INSERT INTO livros 
          (liv_autor, liv_titulo, liv_genero, liv_lancamento, liv_editora, liv_descricao, liv_pags, liv_capa) 
          VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

conn.executemany(sql, books)
conn.commit()
conn.close()