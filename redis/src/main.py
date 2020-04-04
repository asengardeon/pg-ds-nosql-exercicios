import redis
from cartela import Cartela

if __name__ == '__main__':
    r = redis.Redis()
    cartela = Cartela(99, r)
    cartela.criar_cartela("cartalaa", 15)