from crawler.crawler import Crawler

import requests as rq
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

from models.movie import Movie


CATEGORY_CODE = {
    "ALL": "ALL",      # 전체
    "ACTION": "",      # 액션
    "COMEDY": "",      # 코미디
    "DRAMA": "",       # 드라마
    "MELLO": "",       # 멜로
    "HORROR": "",      # 공포/스릴러
    "SF": "",          # SF/판타지
    "ANIMATION": "",   # 애니메이션
    "DOCUMENT": "",    # 다큐멘터리
    "INDEPENDECE": "", # 독립영화
    "": "",            # 공연실황
}

class Naver(Crawler):
  MAX_CNT_OF_PAGE = 25
  PRE_FIX = "NAVER_"

  MOVIES_URL = "https://serieson.naver.com/movie/categoryList.nhn?categoryCode=%s&page=%d"
  DETAIL_URL = "https://serieson.naver.com/movie/detail.nhn?productNo=%s"

  IS_CRAWLER = True

  def __init__(self):
    print('[CALL] Created: Naver Crawler ')

  def get_list(self, page=1, category_code="ALL"):
    is_continue = True

    res = rq.get(Naver.MOVIES_URL % (category_code, page))
    soup = BeautifulSoup(res.content, 'lxml')

    items = soup.select('.lst_thum_wrap .lst_thum li a')
    results = []
    
    Crawler.progress_bar(len(items), 0, 0)

    for idx, item in enumerate(items):
      href, product_no, title, body = self.parse(item)
      movie = Movie(href, product_no, title, body, category_code)
      sleep = 0

      if not movie.is_exist_by_redis(): 
        movie.save_redis()
        results.append(movie)
        sleep = 1
        
      Crawler.progress_bar(len(items), idx+1, sleep)
    
    if len(items) != Naver.MAX_CNT_OF_PAGE:
      is_continue = False

    return is_continue, results

  def detail(self, product_no):
    res = rq.get(Naver.DETAIL_URL % (product_no))
    soup = BeautifulSoup(res.content, 'lxml')
    body = soup.select('#content .end_dsc')

    is_adult = not len(body)
    return '' if is_adult else body[0].text

  def parse(self, item):
    href = item.get('href')
    parts = urlparse(href)
    product_no = parse_qs(parts.query)['productNo'][0]
    title = item.select_one('strong').text
    body = self.detail(product_no)

    return href, '%s_%s'%(Naver.PRE_FIX, product_no), title, body
