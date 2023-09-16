from datetime import datetime as dt
from locale import setlocale, LC_ALL


setlocale(LC_ALL, 'ru_RU')

a = 15


def test_first():
    print(' _ первый этап _ ')
    assert 0
    print(' _ второй этап _ ')
    assert 1


def test_second():
    raise ValueError
    assert 1


def test_third():
    assert a == 15


def test_fourth():
    assert f'{dt.now():%B}' == 'September'


