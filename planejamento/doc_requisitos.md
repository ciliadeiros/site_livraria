# Projeto: Sistema de Biblioteca Virtual “Read On”
**Discentes:** Camila Thaís, Cecília Maria, Demilly Lohany e Filipe Silva

**Turma:** 3° ano de Informática para Internet 1M

O sistema de Biblioteca Virtual “Read On” é uma aplicação que permite o acesso e armazenamento de livros digitais via web, de forma que os usuários possam pesquisar as obras por gênero, autor, título e ano de lançamento, armazenando suas obras favoritas de maneira fácil, rápida e segura. O objetivo desse sistema é permitir que os usuários organizem e acompanhem seus livros em sua própria biblioteca virtual.

O sistema deve conter uma página de cadastro, necessária para que o usuário possa registrar-se no sistema e, assim, ter acesso à página que contém sua biblioteca com seus livros preferidos. Uma vez que o usuário estiver cadastrado, ele poderá acessar novamente a aplicação por meio de uma página de login, que pedirá o e-mail e a senha para verificar se estes coincidem com o que há no banco de dados, garantindo a segurança e a legitimidade das informações. Além disso, haverá a página de livros, que será a principal, onde o cliente poderá visualizar todas as obras disponíveis no catálogo e filtrá-las por suas características. Dessa forma, quando o cliente quiser adicionar um desses exemplares a sua biblioteca pessoal, terá uma página destinada a isso. Essa biblioteca web tem como principal público-alvo usuários interessados em organizar suas leituras, como leitores amadores, estudantes, professores ou clubes do livro.

Ademais, deve haver uma opção de logout, que permite que o usuário desconecte-se da sua conta, além de uma página de contatos que permita que o usuário entre em contato com os desenvolvedores do sistema – em caso de dúvidas, problemas de armazenamento, perda de dados, dentre outros.

# Requisitos Funcionais
O sistema deve:
- Permitir o cadastro de novos usuários;
  
    Possibilitar que novos usuários efetuem seu cadastro para adicionarem livros à sua estante virtual.

- Conter uma página de login, com validação de e-mail e senha;
  
    Uma página de login proporciona uma maior segurança e o controle de acesso a sistemas online, permitindo que apenas usuários autorizados ou logados acessem determinadas informações e serviços. Essa página deve permitir que o usuário insira seu e-mail e senha para acessar sua conta. A partir dessa inserção deve haver uma verificação referente ao formato do email (ex.: nome@escolar.ifrn.edu.br), garantir que a senha não esteja vazia e a seguir regra mínimas (ex: ter pelo menos 6 caracteres, além de um especial), exibir mensagens de erro caso algum dado seja inválido ou incorreto e caso o login seja bem-sucedido, redirecionar o usuário até áreas restritas (ex.: biblioteca pessoal).

- Disponibilizar a opção de logout;
  
    Da mesma forma que se vê necessária uma página de login, é importante existir a opção de logout, permitindo que os usuários encerrem a sessão e mantenham suas obras armazenadas em segurança. Ao clicar no botão de logout (sair), a sessão expira automaticamente e o usuário só consegue ter acesso aos próprios dados caso faça login novamente.
    É uma função importante caso o cliente tenha mais de uma máquina (desktop, notebook, tablet etc) ou trabalhe em um ambiente conjunto, pois, dessa forma, ele previne que outras pessoas acessem seus dados pessoais ao usar a mesma máquina.

- Permitir o acesso à página da estante virtual;
  
    O acesso a página da biblioteca é crucial nesse processo de depósito de dados textuais online, garantindo uma interação efetiva entre o usuário e sua área pessoal. Isso serve para armazenar e gerenciar os produtos de interesse selecionados pelo host (usuário). No sistema proposto, essa página servirá para permitir a visualização, acesso e armazenamento de itens.

- Disponibilizar uma página principal de produtos, com catálogo e filtros;
  
    A página principal de produtos é essencial para o sucesso de qualquer aplicação online, pois ela serve como uma vitrine que possibilita o acesso do usuário aos produtos disponibilizados (livros) por um sistema. Ela deve mostrar os livros disponíveis e funcionar com uma filtragem de características (possibilitando a pesquisa de livros por gênero, autor, título, quantidade de páginas, idioma e entre outros), que são de suma importância para auxiliar o usuário a encontrar o produto de sua preferência e escolha. 
                     
- Ter uma página de contatos para comunicação com os desenvolvedores (dúvidas, problemas, etc.);
  
    Página de contatos é a parte do site que permite uma comunicação direta entre o usuário e administrador. No site o usuário terá acesso a formas de contato, para que qualquer problema (tais quais bugs ou queda de sistema) possa ser relatado e resolvido o quanto antes, além de sugestões para melhorar o site, moldando-o para o público.

# Requisitos Não-funcionais
O sistema deve:
- Possuir uma interface intuitiva (fácil de usar e de compreender);
  
    Uma interface intuitiva é muito importante pois facilita a interação do usuário com um sistema ou software e sem a necessidade de um treinamento para essa interação.

- Ser desenvolvido com Flask, Python e SQLite;

- Possuir um banco de dados (com tabelas de livros, usuários, etc);

- As senhas devem ser armazenadas com hash  seguro (senha criptografada);

- Deve haver validação de e-mail e senha no cadastro e login;

- Apenas usuários logados podem acessar a estante virtual;

- Ter um tempo limite para a sessão do usuário, fazendo logout após um período x de tempo (medida de segurança);
  
    É de suma importância manter a segurança das informações do usuário, e essa medida auxilia em casos de furto, caso alguém roube seu aparelho não poderá acessar a áreas restritas  sem pôr as informações do usuário.
    Após o logout, nenhuma informação do usuário deve permanecer armazenada no navegador;

- Ter documentação;
  
    Possuir uma documentação detalhada do sistema é essencial para uma melhor organização do projeto e para facilitar no processo de produção. A documentação garante que todos os envolvidos entendam a estrutura e o funcionamento do sistema com clarividência, evitando erros por falta de compreensão e tornando a construção do processo mais fácil.


# Referências
**Site:** Skoob

[![App Platorm](https://namanita.com/wp-content/uploads/2015/03/skoob-1.jpg)](https://www.digitalocean.com/products/app-platform)

**Site:** Estante Virtual
[![App Platorm](https://files.tecnoblog.net/wp-content/uploads/2019/09/estante-virtual-site.jpg)](https://www.digitalocean.com/products/app-platform)

