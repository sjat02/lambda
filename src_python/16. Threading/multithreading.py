#I/O tasks | File Operations | Network requests


import threading
from datetime import datetime
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f'Numers is {i}')

def print_letter():
    for letter in 'abcdef':
        time.sleep(2)
        print(f'Letter is {letter}')

#create two thread 

t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letter)


t= time.time()

t1.start()
t2.start()


t1.join()
t2.join()

finished_time = time.time() - t

print(finished_time)


#I/O tasks | File Operations | Network requests

