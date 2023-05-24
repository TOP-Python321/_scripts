def filter_simple(function: 'callable', iterable: list | tuple | str) -> list:
    """Функция высшего порядка: применяет переданный предикат к каждому элементу переданного итерируемого объекта. В результирующем списке возвращает только те элементы, для которых предикат вернул True."""
    result = []
    for item in iterable:
        if function(item):
            result += [item]
    return result


def is_positive(number: float) -> bool:
    """Функция-предикат: проверяет, является ли число положительным."""
    return number > 0


numbers = range(-10, 10)
print(filter_simple(is_positive, numbers))
# print([n for n in numbers if n > 0])


def is_long_word(word: str) -> bool:
    """Функция-предикат: проверяет, что слово состоит из более чем трёх символов."""
    return len(word) > 3


text = """У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил."""

punctuation = '.,:;!?-–—…'
words = map(
    lambda word: word.strip(punctuation), 
    text.lower().split()
)
# words = [
#     word.strip(punctuation)
#     for word in text.lower().split()
# ]
words_filtered = filter_simple(is_long_word, words)
print(*sorted(set(words_filtered)))
