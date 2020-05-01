from crawler.naver import Naver
from time import sleep
from models.movie import Movie
from multiprocessing import Pool, Process

def n(start_page= 1, end_page= 11):
  naver = Naver()

  for page in range(start_page, end_page + 1):
    is_continu, movies = naver.get_list(page, "ALL")
    for movie in movies:
      movie.show()
    
    del movies
    sleep(1)

def get_process_num(num):
  # [(1, 11), (11, 21), (21, 31), (31, 41), (41, 51)]

  return [(i * 10 + 1, (i+1) * 10 + 1) for i in range(0, process_num)]

if __name__ == "__main__":
  process_num = 5

  pages = get_process_num(process_num)
  pool=Pool(process_num)
  procs = []

  for page in pages:
    proc = Process(target=n, args=(page[0], page[1], ))
    procs.append(proc)
    proc.start()

  for proc in procs:
    proc.join()