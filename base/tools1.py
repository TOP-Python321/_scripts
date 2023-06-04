from itertools import repeat, chain
from functools import reduce
from pprint import pprint


class Test:
    pass


repeater_manual = [Test()] * 3
repeater = repeat(Test(), 3)


print(*(id(obj) for obj in repeater_manual), sep='\n', end='\n\n')
print(*(id(obj) for obj in repeater), sep='\n', end='\n\n')


# codes = tuple(range(48, 58)) + tuple(range(65, 91))
codes = chain(range(48, 58), range(65, 91))
digits = {chr(code): i for i, code in enumerate(codes)}

pprint(digits)
print()


numbers = [2, 9, 3, 4, 7, 9, 2, 5]
print(reduce(lambda x, y: x*y, numbers), end='\n\n')


