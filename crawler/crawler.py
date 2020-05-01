# interface

import abc, time, random, sys

class Crawler:
  __metaclass__ = abc.ABCMeta

  @abc.abstractclassmethod
  def get_list(self, page=1, category_code=''):
    pass
  
  @abc.abstractclassmethod
  def get_detail(self, product_no):
    pass


  @classmethod
  def progress_bar(cls, total, current, delay=1, bar_length=30, msg=''):
    percent = float(current) / total
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}% ({2}/{3}{4})".format(arrow + spaces, int(round(percent * 100)), current, total, msg))
    time.sleep(delay)
    sys.stdout.flush()


if __name__ =="__main__":
  Crawler.progress_bar(5, 1)
  Crawler.progress_bar(5, 2)