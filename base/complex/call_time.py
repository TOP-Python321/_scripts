from time import perf_counter as pc


def call_time(function: 'callable'):
    def wrapper(*args, **kwargs):
        start = pc()
        result = function(*args, **kwargs)
        end = pc()
        print(f'время выполнения функции {function.__name__}: {end-start:.6f} с')
        return result
    return wrapper


def is_trivial(number: int):
    for div in range(2, number//2+1):
        if number % div == 0:
            return False
    return True


@call_time
def trivial_numbers(digits: int):
    start = int('1' + '0'*(digits-1))
    end = int('1' + '0'*digits)
    return sum(1 for n in filter(is_trivial, range(start, end)))


print(trivial_numbers(5))
