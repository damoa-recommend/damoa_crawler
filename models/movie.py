from models.connection import REDIS_0, get_mysql_connection
import json

class Movie(object):

  def __init__(self, href, product_no, title, body, category):
    self.href = str(href)
    self.product_no = str(product_no)
    self.title = str(title)
    self.body = str(body.replace('\n', '').replace('\t', '').replace('\r', '').replace('  ', ''))
    self.category = str(category)

  def save(self):
    self.save_mysql()
    self.save_redis()

  def save_mysql(self):
    sql = '''
      INSERT INTO Movies 
        (href, productNo, title, body, category) 
      VALUES 
      (%s, %s, %s, %s, %s)
    '''
    
    cursor, mysql = get_mysql_connection()
    cursor.execute(sql, (self.href, self.product_no, self.title, self.body, self.category))
    mysql.commit()

  def save_redis(self):
    REDIS_0.set(self.product_no, json.dumps({
      "href": self.href,
      "product_no": self.product_no,
      "title": self.title,
      "body": self.body,
      "category": self.category
    }))

  def show(self):
    print('href: %s, product_no: %s, title: %s, category: %s'%(self.href, self.product_no, self.title, self.category))
    print('body: %s'%(self.body))
    print()


  def get(self):
    return REDIS_0.get(self.product_no)

  def is_exist_by_redis(self):
    return not not self.get()