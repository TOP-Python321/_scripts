from random import randrange as rr
from pathlib import Path
from sys import path


SCRIPT_DIR = Path(path[0])
TARGET = SCRIPT_DIR / 'files4.txt'


words = []
for _ in range(100):
    word = ''.join(chr(rr(97, 123)) for _ in range(rr(4, 10)))
    words += [word]

with open(TARGET, 'w', encoding='utf-8') as fileout:
    for word in words:
        print(word, end=' # ', file=fileout)

