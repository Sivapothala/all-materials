import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i*i}")

def Cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube : {i*i*i}")

## Create 2 processes
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=Cube_numbers)
    t = time.time()
    ## Start the Process

    p1.start()
    p2.start()

    ##wait for the process
    p1.join()
    p2.join()

    finstime = time.time() -t
    print(finstime)