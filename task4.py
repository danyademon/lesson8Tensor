import numpy
import time

last_start = 0.0

def decorator_log_and_time_and_frequency(func):
    def wrapper(*args):
        global last_start
        if time.time() - last_start < 3:
            print('Сейчас нельзя запустить эту функцию, подождите.')
            return 0
        with open('log.txt', 'a', encoding='utf-8') as output:
            output.write(f'{func.__name__} Started\n')
            start = time.time()
            res = func(*args)
            print(f'Время выполнения функции: {func.__name__}: {time.time() - start}')
            output.write(f'{func.__name__} Ended\n')
        last_start = time.time()
        return res
    return wrapper

@decorator_log_and_time_and_frequency
def random_func(x,y):
    a = numpy.random.sample((x,y))
    return a

matrix = random_func(1000,10000)
matrix = random_func(1000,10000)
time.sleep(3)
matrix = random_func(1000,10000)
