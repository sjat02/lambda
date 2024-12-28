#dividing the workload acrosss different cores of CPU

import multiprocessing
import sys
import time
import math


sys.set_int_max_str_digits(100000)

## function to compute factorial of a given number

def compute_fact(number):
    print(f"Computing factorial of a {number}")
    result = math.factorial(number)
    print(f'Factorial of a {number} is {result}')
    return result



if __name__ == '__main__':
    numbers = [5000,6000,7000,8000]
    start= time.time()

    #create a pool of worker

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_fact,numbers)
        
    finished_time = time.time() - start

    print(results)
    print(f'Time taken is {finished_time}')

