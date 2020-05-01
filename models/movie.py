from models.connection import REDIS_0, MYSQL
import json

class Movie(object):

  def __init__(self, href, product_no, title, body, category):
    self.href = href
    self.product_no = product_no
    self.title = title
    self.body = body.replace('\n', '').replace('\t', '').replace('\r', '').replace('  ', '')
    self.category = category

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