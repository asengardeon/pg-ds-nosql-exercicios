from random import randint

import redis
from cartela import Cartela, NUMEROS_POSSIVEIS_KEY
from jogador import Jogador

if __name__ == '__main__':
    r = redis.Redis()
    jogadores = []
    for n in range(50):
        jogadores.append(Jogador("user"+str(n), r))

    for jogador in jogadores:
        print(r.hgetall(jogador.player))
        cartela = r.hget(jogador.player, "cartela")

    tem_vencedor = False
    jogador_vencedor = ""
    while not tem_vencedor:
        num = randint(0, 99)
        for jogador in jogadores:
            cartela = r.hget(jogador.player, "cartela")
            if r.sismember(cartela, num):
                r.hincrby(jogador.player, "score", 1)
            if r.hget(jogador.player, "score") == 15:
                tem_vencedor = True
                jogador_vencedor = jogador.player

    print("O jogador  vencedor foi: %s".format(jogador_vencedor))
