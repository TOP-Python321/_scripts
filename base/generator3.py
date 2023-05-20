from random import choice, randrange as rr
from string import ascii_lowercase as latin


def random_strings(words_number: int) -> 'generator':
    """Генерирует случайные буквосочетания используя латинский алфавит."""
    for _ in range(words_number):
        word = ''.join(
            choice(latin)
            for _ in range(rr(3, 9))
        )
        cap_probability = [0, 0, 0, 1]
        yield (word, word.capitalize())[choice(cap_probability)]


print(*random_strings(20))
