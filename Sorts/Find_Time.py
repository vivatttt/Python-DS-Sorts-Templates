import time

def find_time(func):
    def wrapper(*args, **kwargs):
        '''
        Засекаем время выполнения различных функций сортировки
        '''
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения {func.__name__} = {end - start}')
        return result         
    return wrapper