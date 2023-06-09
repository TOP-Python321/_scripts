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
Свои мне сказки говорил.
"""

text_lower = text.lower()

# ручной способ выделения знаков препинания
# punctuation = '.,:;!?-–—'

cyrillic = {chr(code) for code in range(1072, 1104)} | {'ё'}
space = {' ', '\n'}
punctuation = ''.join(set(text_lower) - cyrillic - space)


# быстрый способ — без создания полного списка слов, очищенных от знаков препинания
words_count = {}
for word in text_lower.split():
    word_clean = word.strip(punctuation)
    # использование словарного метода get()
    words_count[word_clean] = words_count.get(word_clean, 0) + 1


# создание полного списка слов, очищенных от знаков препинания
# words = []
# for word in text_lower.split():
    # word_clean = word.strip(punctuation)
    # if word_clean:
        # words += [word_clean]

# то же самое с использованием генераторного выражения
words = [
    word_clean
    # использование строкового метода split()
    for word in text_lower.split()
    # использование строкового метода strip()
    if (word_clean := word.strip(punctuation))
]


# создание словаря уникальных слов с частотой их использования в исходной строке
# words_count = {}
# for word in set(words):
    # words_count[word] = words.count(word)

# то же самое с использованием генераторного выражения
words_count = {
    # использование метода последовательностей count()
    word: words.count(word)
    for word in set(words)
}


# сортировка
# words_count_ord = dict(sorted(
    # words_count.items(), 
    # использование анонимной функции, возвращающей ключ сортировки
    # key=lambda x: x[1], 
    # reverse=True
# ))

print(*[
    f'{word}: {rate}'
    for word, rate in words_count.items()
    if rate > 1 and len(word) > 2
], sep='\n')

