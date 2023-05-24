def process_text(word_processor: 'callable', 
                 char_processor: 'callable', 
                 text: str) -> str:
    result = []
    for word in text.split():
        word_edit = ''
        for char in word:
            word_edit += char_processor(char)
        result += [word_processor(word_edit)]
    return ' '.join(result)


def caesar(char: str, shift: int = 1) -> str:
    code = ord(char) 
    if code in range(65, 91):
        return chr((code+shift-65) % 26 + 65)
    elif code in range(97, 123):
        return chr((code+shift-97) % 26 + 97)
    elif code in range(1040, 1072):
        return chr((code+shift-1040) % 32 + 1040)
    elif code in range(1072, 1104):
        return chr((code+shift-1072) % 32 + 1072)
    else:
        return char

def reverse(word: str) -> str:
    return word[::-1]


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

coded = process_text(reverse, caesar, text)
print(coded, end='\n\n')

decoded = process_text(reverse, lambda char: caesar(char, -1), coded)
print(decoded, end='\n\n')
