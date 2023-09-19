"""
Рамочные автотесты (TDD) для класса app.utils.file_io.FileIO
"""

from pathlib import Path
from sys import path
from tomllib import loads

from app.utils import FileIO


# для отключения перехвата и отображения вывода в окне терминала выполнять pytest с ключом -s
# print('\n\ntest_file_io', *path, sep='\n', end='\n\n')

ROOT_DIR = Path(path[1]).parent
config = loads((ROOT_DIR / 'pyproject.toml').read_text(encoding='utf-8'))


def test_singleton():
    """Проверка Одиночки."""
    inst1 = FileIO()
    inst2 = FileIO()
    assert inst1 is inst2


def test_default_path():
    """Проверка пути по умолчанию."""
    expected = ROOT_DIR / config['paths']['history']
    inst = FileIO()
    assert expected == inst.history_log


def test_non_default_path():
    """Проверка переопределения пути."""
    expected = str(ROOT_DIR / path[0])
    inst = FileIO(expected)
    assert Path(expected) == inst.history_log


class TestIO:
    """
    Проверка операций чтения/записи.
    """
    file_path = ROOT_DIR / config['paths']['history_test']
    inst = FileIO(file_path)


    def test_write_operation(self):
        """Запись одной операции."""
        expected = '1 + 2 = 3'
        self.inst.write_operation(expected)
        # в некоторых тестах по разным причинам мы хотим максимально обезопаситься от потенциальных исключений, которые могут возникнуть не из тестируемого кода, и ради этого жертвуем производительностью
        last_row = None
        # например, если операция записи тестируемым файлом выполнена некорректно или не выполнена, а тестовый файл при этом пустой или отсутствует, то отсутствие ветвлений приведёт к возникновению исключения в тесте, но не в тестируемом классе/методе
        if self.file_path.is_file():
            rows = self.file_path.read_text(encoding='utf-8').split('\n')
            if rows:
                # а в текущей структуре кода переменная last_row точно будет существовать и будет равна либо None либо str объекту
                last_row = rows[-1]
        assert expected == last_row


    def test_read_operation(self):
        """Чтение одной операции."""
        expected = '4 + 5 = 9'
        with open(self.file_path, 'a', encoding='utf-8') as test_file_out:
            print(expected, file=test_file_out)
        last_row = self.inst.read_operation()
        assert expected == last_row


    def test_read_all(self):
        """Чтение одной операции."""
        expected = [
            '2 + 8 = 10\n',
            '4 - 6 = -2\n',
            '0 ^ 1 = 1\n',
        ]
        with open(self.file_path, 'w', encoding='utf-8') as test_file_out:
            test_file_out.writelines(expected)
        all_rows = self.inst.read_all()
        assert expected == all_rows

