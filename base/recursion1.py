def test_recur1():
    print('я — рекурсивная функция')
    test_recur1()


try:
    test_recur1()
except RecursionError:
    pass


def recur_counter(n: int):
    if n <= 0:
        print(f'последний шаг рекурсии {n = }')
    else:
        print(f'перед рекурсивным вызовом {n = }')
        recur_counter(n-1)
        print(f'после рекурсивного вызова {n = }')


recur_counter(5)
print('все рекурсивные вызовы выполнены')

