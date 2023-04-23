left = ord('а')
right = ord('я')

vowels_cyr = 'аеиоуыэюя'

letters_cyr = (
    # 4. вычисляется выражение
    char.upper() + char
    # 1. вычисляется итератор
    # 2. начинается цикл
    for code in range(left, right+1)
    # 3. проверяется логическое выражение
    if (char := chr(code)) not in vowels_cyr
)

print(*letters_cyr, sep=', ')
