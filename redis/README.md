# Exercicios REDIS

Este projeto é  um jogo  de bingo para 50 competidores, desenvolvido em python + redis


## Pre-requisito
* Python 3.8
* Pipenv
* Redis server

## Baixando dependencias
O projeto utiliza uma biblioteca redis para se comunicar com o servidor  que  deve estar rodando localmente.

Para  baixar as dependencias deve-se  executar o  comando abaixo na raiz do  peojto, onde esta localizado o arquivo  PipFile:

~~~shell
$ pipenv install
~~~

## Executando o projeto
O  projeto excuta  uma vez apresentando  no  terminal os jogadores criados e as cartelas criadas para cada jogador. 
Ao  final da execução é  apresentado o jogador vencedor.

Para executar o projeto é  necessário executar o  arquivo  main.py que esta no diretório src, estando na raiz do  projeto.

~~~shell
$ python src/main.py
~~~




