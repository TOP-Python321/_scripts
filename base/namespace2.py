from pprint import pprint

# pprint(globals())
# pprint(locals())
# print()

def main(arg1, arg2):
    # pprint(globals())
    pprint(locals())
    print()
    
    a = arg1 + arg2
    a += b
    
    # pprint(globals())
    pprint(locals())
    print()
    
    return a


a = 'variable a'
b = 'variable b'

test_str = main(a, b)

# pprint(globals())
# pprint(locals())
# print()

main(test_str, a)

# pprint(globals())
# pprint(locals())
# print()
