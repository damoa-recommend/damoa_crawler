import redis
from config.config import config
import pymysql

REDIS_0 = redis.Redis(
  host=config['redis']['HOST'], 
  port=config['redis']['PORT'], 
  db=0
)


def get_mysql_connection():
  MYSQL = pymysql.connect(
    user=config['mysql']['USER'] ,
    passwd=config['mysql']['PASSWORD'] ,
    host=config['mysql']['HOST'] ,
    db=config['mysql']['DB'] ,
    charset='utf8'
  )
  return MYSQL.cursor(pymysql.cursors.DictCursor), MYSQL