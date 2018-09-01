# Sobre os arquivos do branch Master  

`DESENVOLVENDO.md`

Arquivo para demonstrar como fazer teste e desenvolver o bot em sua máquina local.

`Procfile`

é um arquivo que faz parte do servidor [heroku](https://www.heroku.com/). Ele indicada o comando a ser executado pelo dynos, que é aonde nosso bot, a aplicação, é
inicializada dentro do heroku, [dynos](https://devcenter.heroku.com/articles/dynos) são chmamados de containers.

detalhe importante, o arquivo não tem extensão declarada.

[Sobre Procfile](https://devcenter.heroku.com/articles/procfile)

`README.md`

é o arquivo que explica e inicializa o projeto. Cada diretório pode ter seu README.me próprio.

[Sobre README](https://pt.wikipedia.org/wiki/Readme)

`__init__.py`

é um arquivo conhecido nos módulos python. Está no diretório do projeto para indicar ao interpretador python que aqui tem arquivos python!  

[Sobre __init__.py](https://pt.stackoverflow.com/questions/96608/para-que-serve-o-arquivo-init-py-em-m%c3%b3dulos-no-python#96796)

`requirements.txt`  

é um arquivo feito pelo gerenciador de pacotes [pip](https://pt.wikipedia.org/wiki/Pip_gerenciador_de_pacotes). Ele analisa o ambiente da aplicação e registra todos os módulos presentes no diretório. Depois faz uma lista especificando o que o servidor terá que constuir, fazendo o buildpacks do servidor.

[Sobre requirements.txt](https://pip.readthedocs.io/en/1.1/requirements.html)

`runtime.txt`  

é um arquivo que faz parte da construção do buildpack, dizendo qual a versão que a linguagem da aplicação está rodando.

[Sobre runtime.txt](https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-python) <sub>final da página<sub>

`sugestões.md`

é um arquivo para sugerimos funcionalidades para o bot.

`zumpy.py`

é o arquivo principal do bot, ele que é inicializado pelo servidor.



