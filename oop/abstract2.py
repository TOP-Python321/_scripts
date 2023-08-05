from abc import ABC, abstractmethod
from pathlib import Path


# абстрактный базовый класс: первый (корневой) уровень абстракции
class MusicalInstrument(ABC):
    @abstractmethod
    def play(self, tone: str) -> bytes:
        pass


# абстрактный производный класс: второй уровень абстракции.
class Acoustic(MusicalInstrument):
    def __init__(self, lowest: str, highest: str):
        self.range = (lowest, highest)


# абстрактный производный класс: второй уровень абстракции.
class Synthetic(MusicalInstrument):
    @abstractmethod
    def modulate(self, shift: str) -> bytes:
        pass


# абстрактный производный класс: третий уровень абстракции.
class Keyboard(Acoustic):
    def __init__(self, lowest: str, highest: str, mechanics):
        super().__init__(lowest, highest)
        self.mechanics = mechanics


# абстрактный производный класс: третий уровень абстракции.
class String(Acoustic):
    def __init__(self, lowest: str, highest: str, *strings: str):
        super().__init__(lowest, highest)
        self.number = len(strings)
        self.strings = strings


# класс-реализация
class Piano(Keyboard):
    __samples_dir_path: Path = Path('')

    def play(self, tone: str) -> bytes:
        with open(self.__samples_dir_path / f'{tone}.wav', 'b') as wavfile:
            return wavfile.read()



class Player:
    """
    Проигрыватель.
    """
    def __init__(self, instrument: MusicalInstrument):
        self.instrument = instrument

    def play(self, melody: list[str], **options):
        for tone in melody:
            self.instrument.play(tone)

