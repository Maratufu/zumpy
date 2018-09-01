# [@ZumpyBot](https://telegram.me/zumpybot)   
   Versão 0.0  
Curso [Python para Zumbis](https://www.pycursos.com/python-para-zumbis/)  
de Fernando Massonori.  

Status: &nbsp; 🚧

___

A idéia desse projeto é aplicarmos a linguagem Python e desenvolver um BOT com a função de auxiliar o grupo do [Telegram](https://t.me/joinchat/G8b9FA5W3DVK_rvcdSIKzA) Python Para Zumbis.

Também será uma maneira de familiarizamos com a estrutura de projetos e aplicações. Por isso utilizaremos o sistema de controle `Git` e um serviço de hospedagem em nuvem para a realização do deploy.

####  `Mega importante`

  Projeto totalmente didático. O intuito aqui é aprender, portanto seria muito bom termos a prática de explicar e orientar as pessoas sobre qualquer alteração no código e no projeto.


___  

## Só para avisar

`ARQUIVOS.md`

Mostra um pouco sobre o que é cada arquivo no [branch](https://pt.stackoverflow.com/questions/20989/qual-significado-de-branch-tag-e-trunk/20996#20996) Master.

`README.md`

É esse arquivo que você está lendo.

**dica**: abrir os links segurando a **tecla** de atalho para nova aba.

`DESENVOLVENDO.md`

Arquivo que descreve como testar e desenvolver o bot antes de fazer algum commit.

___

## O que é ...

### [Git](https://git-scm.com/)
  é um sistema de controle de versões de um projeto. Criado sobre licença [GPL-2.0](https://opensource.org/licenses/GPL-2.0) e muito usado no desenvolvimento de aplicações. No caso, utilizaremos o GitHub, que é um serviço de hospedagem e gerenciamento de projeto que dialoga junto com o Git.

  * [Sobre Git e GitHub](https://tableless.com.br/tudo-que-voce-queria-saber-sobre-git-e-github-mas-tinha-vergonha-de-perguntar/)
  * [Usando Git](https://rogerdudler.github.io/git-guide/index.pt_BR.html)


### [Markdown](https://daringfireball.net/projects/markdown/)
  é uma linguagem para edição de textos, inclussive esse texto está sendo feito em Markdown, reparem a extensão do arquivo `.md`

  + [Sobre Markdown](https://www.markdownguide.org/basic-syntax)


### [Heroku](https://www.heroku.com/)

  é um serviço de hospedagem em nuvem que permite deixarmos rodando uma aplicação, que é o caso de fazer um deploy, quando você tira sua aplicação no modo desenvolvimento e passa para o de produtividade.

  + [Sobre Heroku e Deploy de bot](https://medium.com/@rafaelvicio/hospedando-seu-bot-no-heroku-60a9b5ed709a)

### [python-telegram-bot](https://python-telegram-bot.org/)

  é uma biblioteca específica para desenvolver bots em python. Usa diretamente a API do Bot Telegram.

  `mas por que usar uma biblioteca?`

  >The telegram.ext submodule is built on top of the pure API implementation. It provides an easy-to-use interface and takes some work off the programmer, so you [don't have to repeat yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).
  >
  >`pt-br`  
  O sub módulo telegram.ext é construído puramente em cima da API de implementação. Isso proporciona uma interface fácil de utilizar e você [não precisa ficar se repetindo](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).


  + [Sobre python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/)

  ---

## Por onde começar?
_Utilizo o sistema OSX alguns aplicativos/funções possam diferenciar do seu sistema._  

Primeiro passo é clonar esse repositório para sua máquina. Assim poderá editar e enviar arquivos para esse projeto.

### Como clonar  
_* Se você já tiver o GitHub Desktop, só clicar em Open in Desktop_

![](https://a.imagem.app/2fRk0.png)


##### GitHub Desktop  


Recomendo usar com o [GitHub Desktop](https://desktop.github.com/) que por sinal é integrado com o editor [Atom](https://atom.io/), facilitando abrir o projeto no próprio editor.

![gdsk](https://a.imagem.app/2fErW.png)

ou

##### Terminal
  -  Usar o git pelo terminal só se você tiver domínio do que está fazendo.


    git clone https://github.com/Maratufu/zumpy.git

esse comando irá clonar na pasta em que você estiver acessando no terminal.


### Modificando versões ou adicionando arquivos

> Lembrando que você pode fazer tudo pelo próprio GitHub, editar, adicionar, fazer commit entre outras coisas. Basta ter uma conta logada e verificada, abaixo vou comentar rapidinho usando um editor de texto.   

Com o repositório clonado, de forma resumida, digamos que você tem um "espelho" do projeto em sua máquina. Qualquer alteração no diretório local será comparado posteriormente com a versão do projeto no GitHub.

![](https://s8.postimg.cc/mr0umez2d/Captura_de_Tela_2018-08-30_a_s_20.47.29.png)

Para modificar um arquivo já existente, é só abrir com seu editor de preferência e depois salvar a modificação. Caso for um novo arquivo, você deve salvar na pasta do repositório em seu computador e seguir os passos orientado pelo git.

>Novamente, caso for utlizar o `terminal`, recomendo seguir as orientações do [site](https://rogerdudler.github.io/git-guide/index.pt_BR.html) já mencionado.

Para quem for usar o Atom a interface para o commit é bem tranquila. No exemplo abaixo vou alterar o arquivo `sugestoes.md`

![](https://s8.postimg.cc/k9p3f6pgl/Captura_de_Tela_2018-08-30_a_s_21.38.35.png)

_Para logar com o GitHub no Atom é só seguir os passos que vão aparecer na interface do GitHub Tab._

Repara que depois de salvo o arquivo já **destaca** a cor na arvore do projeto que foi modificado, a mesma cor aparece no código indicando o que foi adicionado.

Na parte do GitHub Tab vocês vão acionar os comandos que se referem ao Git. O `StageAll` ele faz os arquivos serem indexados para realizar o `commit`.

![](https://s8.postimg.cc/gq35pck5x/Captura_de_Tela_2018-08-30_a_s_22.23.47.png)

Depois é só adicionar um comentário explicando o que está sendo alterado e depois realizar o commit.


![](https://s8.postimg.cc/i54qe38ed/Captura_de_Tela_2018-08-30_a_s_21.51.24.png)

A ação que faz o commit ser enviado para o repositório do projeto é o `Push` - Quando for remover/receber alguma versão a opção será `Pull` -

![](https://s8.postimg.cc/y3dg47n6t/Captura_de_Tela_2018-08-30_a_s_21.53.56.png)

`Regra Branch Master`

 Quando realizar essa ação a nova versão será enviada para um branch novo, e será comparado com o Master. Depois das votações e verificações, caso aprovado, o branch será substituído, e consequemente o bot irá ser atualizado também.

>Como o bot já está rodando e vinculado para o [servidor](http://heroku.com/) atualizar automaticamente pelo GitHub quando um push ou pull for concluído, no branch Master devemos verificar antes a mudança da versão para evitar problemas, por isso o uso da regra no branch.  
