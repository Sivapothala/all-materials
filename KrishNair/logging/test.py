from logger import logging

def add(a,b):
    logging.debug("the addition operation is taking place")
    return a+b

logging.debug("calling the add function")
print(add(6,5))