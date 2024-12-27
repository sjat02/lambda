#Processes that runs parallel
# multiple cores in CPU

import multiprocessing
import multiprocessing.process
import time

def sqares_num():
    for i in range(5):
        time.sleep(2)
        print(f'Sqare is {i**2}')

def cube_num():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube is {i**3}')


if __name__ == '__main__':

    p1 = multiprocessing.Process(target=sqares_num)
    p2 = multiprocessing.Process(target=cube_num)


    t = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()



    finish_time = time.time() - t
    print(finish_time)