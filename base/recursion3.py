data1 = [
    12,
    '345',
    (6, 7),
    {
        'a': 8,
        'b': 9,
        'c': 10
    },
    1.1,
    [
        (0.12, 0.13, 0.14),
        (0.15, 0.16, 0.17),
    ]
]
data2 = [
    'a',
    'b',
    ['c', 'd', 'e'],
    (
        {'f': 1, 'g': 2, 'h': 3},
        {'i': 1, 'j': 2, 'k': 3}
    ),
    'mn',
    'op',
    {
        'q': {
            'r': {10, 20, 30}
        },
        's': {
            't': {40, 50, 60}
        },
    }
]

from collections.abc import Iterable

def extractor(data: Iterable) -> list:
    result = []
    
    if isinstance(data, dict):
        data = list(data.values())
    
    for elem in data:
        if isinstance(elem, Iterable) and not isinstance(elem, str):
            result += extractor(elem)
        else:
            result += [elem]
    
    return result


