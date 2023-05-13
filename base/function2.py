# приведёт к выбросу исключения NameError:
# test_function()


def test_function():
    test_function_2()


def test_function_2():
    print('вызов test_function_2')


# не приведёт к исключению
test_function()
