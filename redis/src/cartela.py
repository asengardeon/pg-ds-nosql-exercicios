from redis import Redis

NUMEROS_POSSIVEIS_KEY = "nuemros_possiveis_cartela"

class Cartela:

    def __init__(self, quantidade_numeros_possiveis: int, client_redis: Redis):
        self.numeros_possivels = quantidade_numeros_possiveis
        for n in range(quantidade_numeros_possiveis):
            client_redis.sadd(NUMEROS_POSSIVEIS_KEY, n)
        self.client_redis = client_redis


    def criar_cartela(self, key: str, quantidade_numeros: int):
        for _ in range(quantidade_numeros):
            self.client_redis.sadd(key, self.client_redis.srandmember(NUMEROS_POSSIVEIS_KEY))


