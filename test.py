import time
import os

from multiprocessing import Pool, Process

def do_work(n):
  print('value', n, 'PID:', os.getpid())
  
  for i in range(0, n):
    print('value', i, 'PID:', os.getpid())
    if n %2 : 
      time.sleep(4)
    else:
      time.sleep(2)

if __name__ == "__main__":
  pool=Pool(3)
  nums= [4, 1, 4, 3]
  procs = []

  for idx, n in enumerate(nums):
    proc = Process(target=do_work, args=(n, ))
    procs.append(proc)
    proc.start()

  for proc in procs:
    proc.join()