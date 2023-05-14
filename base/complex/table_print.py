#  1   4
# 17 100
#  3  12

def table_print(table: list[list[int]],
                *,
                col_sep: str = ' ',
                row_sep: str = '-',
                align: str = 'right') -> str:
    """Возвращает строковое табличное представление чисел."""
    alignment = {
        'left': '<',
        'center': '^',
        'right': '>',
    }
    max_width = max(
        len(str(num)) 
        for row in table for num in row
    )
    rows = [
        col_sep.join(
            f"{str(num):{alignment[align]}{max_width}}" 
            for num in row
        )
        for row in table
    ]
    full_width = max(len(row) for row in rows)
    horiz_line = row_sep*full_width
    return f'\n{horiz_line}\n'.join(rows)


print(table_print.__name__)
print('\t', table_print.__annotations__)
print('\t', table_print.__doc__, '\n')

numbers = [
    list(range(50, 150, 10))
    for _ in range(5)
]
print(numbers, '\n')
print(table_print(numbers, col_sep='|', row_sep='~', align='left'))
