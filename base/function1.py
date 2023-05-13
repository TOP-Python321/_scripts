def test_function():
    print('функция test_function')
    pass


def test_function_2():
    print('функция test_function_2')
    for _ in range(5):
        print(end='\t')
        test_function()
        pass


print('начало программы')
test_function_2()
print('конец программы')

