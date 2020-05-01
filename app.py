from crawler.naver import Naver
from time import sleep
from models.movie import Movie
from multiprocessing import Pool, Process
import click, sys


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

  return [(i * 10 + 1, (i+1) * 10 + 1) for i in range(0, num)]


@click.command()
@click.option('-p', '--procs', default=1, help="Process Number")
@click.option('-v', '--version', is_flag=True, help="Show version of this program.")
# @click.argument('start')
def main(version, procs):
  if version:
    print('Version: 1.0.0')
    sys.exit()

  pages = get_process_num(procs)
  procs = []

  for page in pages:
    proc = Process(target=n, args=(page[0], page[1], ))
    procs.append(proc)
    proc.start()

  for proc in procs:
    proc.join()

if __name__ == "__main__":
  main()