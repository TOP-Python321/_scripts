scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}


def erudit(word: str) -> int:
    # изменяется (без пересоздания) глобальная переменная scores_letters
    scores_letters[1] += 'Ё'
    return sum(
        score
        for score, letters in scores_letters.items() 
            for char in word.upper()
        if char in letters
    )


var = 1

def test():
    # получение доступа на запись к глобальному пространству имён
    global var
    # print(a)
    # без global здесь создаётся локальная переменная var, с global пересоздаётся глобальная переменная var
    var = 3
    print(var)


print(var)

