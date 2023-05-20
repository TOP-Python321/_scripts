def text_parse(text: str, word_processor: 'function') -> None:
    """Разбивает текст на слова, применяет к каждому слову переданный обработчик, выводит результат в stdout."""
    for word in text.split():
        print(word_processor(word))


text = """Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable."""

text_parse(text, lambda word: word.strip('.,:;!?()'))
print()

text_parse(
    text.lower(), 
    lambda word: ''.join(
        chr((ord(ch) - 94) % 26 + 97) 
            if ch.isalpha() else 
        ch 
        for ch in word
    )
)
