"""Single Responsibility Principle — Принцип Единственной Ответственности"""

from datetime import datetime as dt
from pathlib import Path
from sys import path


class Journal:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, text: str):
        self.entries.append((dt.now(), text))
    
    # метод write_file() нарушает SRP, т.к. единственная ответственность класса Journal — это предоставление интерфейса для работы со структорой данных
    # def write_file(self, file_path: Path):
        # text = '\n'.join(
            # f'{timestamp:%Y-%m-%d %H:%M:%S} — {text}'
            # for timestamp, text in self.entries
        # )
        # file_path.write_text(text, encoding='utf-8')


# решение — выделить ответственность по взаимодействию с объектами файловой системы в отдельный класс
class FileSystemIO:
    __default_log_path: Path = Path(path[0]) / 'solid_SRP.log'
    
    @classmethod
    def write_log(cls, journal_instance: Journal, file_path: Path = None) -> Path:
        text = '\n'.join(
            f'{timestamp:%Y-%m-%d %H:%M:%S} — {text}'
            for timestamp, text in journal_instance.entries
        )
        if file_path is None:
            file_path = cls.__default_log_path
        file_path.write_text(text, encoding='utf-8')
    
