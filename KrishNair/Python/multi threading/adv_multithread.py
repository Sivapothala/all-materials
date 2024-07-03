### Multithreading with thread pool executor

# from concurrent.futures import ThreadPoolExecutor
# import time

# def print_number(number):
#     time.sleep(1)
#     return f"Number : {number}"


# numbers = [1,2,3,4,5,6,7,8,6,6,5,4,3,2,1]

# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(print_number,numbers)

# for result in results:
#     print(result)


### MultiProcessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"Square : {number*number}"


numbers = [1,2,3,4,5]
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,numbers)

    for result in results:
        print(result)