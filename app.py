from crawler.naver import Naver
from time import sleep
from models.movie import Movie

NAVER_PAGE = 1

if __name__ == "__main__":
  naver = Naver()
  
  while naver.IS_CRAWLER:
    is_continu, movies = naver.get_list(NAVER_PAGE, "ALL")
    
    for movie in movies:
      movie.show()
    sleep(1)

    NAVER_PAGE += 1