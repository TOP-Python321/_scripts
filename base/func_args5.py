def test_function(pos_arg, *args, key_arg, **kwargs):
    print(pos_arg)
    print(args)
    print(key_arg)
    print(kwargs)
    print()


test_function(1, key_arg=2)
test_function(1, 2, 3, key_arg=4, key2=5, key3=6)

numbers = range(1, 10)
params = {'a': 2, 'b': 3, 'key_arg': 4}

test_function(*numbers, **params)
