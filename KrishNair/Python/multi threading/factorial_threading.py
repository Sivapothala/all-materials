'''
Real world Example : Multiprocessing for CPU-bound Tasks
Scenario : Factorial Calculation
Factorial calcualtions,espcially for large numbers,
involves significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores,improving performance

'''

import multiprocessing
import math
import sys
import time

#Increase the maximum numbers of digits for integer conversion
sys.set_int_max_str_digits(100000)


##  Function to compute factorial of a given number
def computer_factorial(number):
    print(f"Computing factorial of a Number of {number}")
    result = math.factorial(number)
    return result

if __name__ == "__main__":
    numbers = [500,600,700,800]
    # numbers = [5,100]
    start_time = time.time()

    ## Create a pool of workers processes
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial,numbers)

    endtime = time.time()
    print(f"total time : {endtime-start_time}")
    print(f"Results : {results}")
    print("All Done")