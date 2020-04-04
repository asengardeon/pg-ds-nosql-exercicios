from redis import Redis

from cartela import Cartela


class Jogador:

    def __init__(self, nome: str, client_redis: Redis):
        self.client_redis = client_redis
        self.nome = nome
        self.player = "user:" + nome

        nome_cartela = "cartela:" + nome
        cartela = Cartela(99, client_redis)
        cartela.criar_cartela(nome_cartela, 15)
        client_redis.hset(self.player, "name", self.nome)
        client_redis.hset(self.player, "cartela", nome_cartela)
        client_redis.hset(self.player, "score", "0")
