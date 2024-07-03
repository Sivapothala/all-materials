import logging

## logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    #handlers are the other type parameter to decide which file we have to store the log data. of type list
    #stream handler is responsible for putting the logs into the specified files.
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
    )

logger = logging.getLogger("ArithmaticApp")

def add(a,b):
    result = a+b
    logger.debug(f"adding {a} and {b} = result {result}")
    return result

def Subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a} and {b} = result {result}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"multiplying {a} and {b} = result {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"adding {a} and {b} = result {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero Error")
        return None
    

add(10,15)
Subtract(56,10)
multiply(10,79)
divide(10,2)