"""
Controller (MVC): управляющий модуль, точка входа.
"""

import model
import view_cli as view
# import view_gui as view


def start() -> None:
    view.start_view()


def get_command():
    while True:
        command: str = view.get_command_view()

        if command == 'all':
            get_all_people()

        elif command.startswith('langs'):
            langs = command.split()[1:]
            get_people_by_lang(langs)

        elif command == 'quit':
            break


def get_all_people():
    people = [str(person) for person in model.storage]
    view.show_people(people)


def get_people_by_lang(langs: list[str]):
    langs = set(langs)
    people = [
        str(person)
        for person in model.storage
        if langs <= person.langs
    ]
    view.show_people(people)


def end():
    view.end_view()


def main() -> None:
    model.storage = model.read_all_people()
    start()
    if 'CLI' in view.__doc__:
        get_command()
    end()



# точка входа
if __name__ == '__main__':
    main()
