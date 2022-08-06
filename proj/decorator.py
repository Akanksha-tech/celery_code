
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


def logger(func):
    def log_func(*args):
        logging.info('Running {} with args {}'.format(func.__name__,args))
        print(func(*args))
    return log_func

fun = logger(add)
fun(2,2,2)

