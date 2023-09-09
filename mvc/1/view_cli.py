"""
View (MVC): CLI представление.
"""


def start_view() -> None:
    print('\nДобро пожаловать в Демонстратор MVC!')


def get_command_view() -> str:
    return input('\n > ')


def show_people(data: list[str]) -> None:
    print(*data, sep='\n')


def end_view() -> None:
    print('\nПока!')
