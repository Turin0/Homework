import time
from threading import Thread

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
num_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def stream(*args):
    for _ in args:
        time.sleep(1)
        print(_, flush=True)


thread_N = Thread(target=stream, args=list(num_))
thread_L = Thread(target=stream, args=list(letter))
thread_N.start()
time.sleep(0.01)
thread_L.start()

thread_N.join()
thread_L.join()
