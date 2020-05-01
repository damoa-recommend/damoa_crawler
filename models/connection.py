import redis
from config.config import config

REDIS_0 = redis.Redis(host=config['redis']['HOST'], port=config['redis']['PORT'], db=0)

MYSQL_ = ''