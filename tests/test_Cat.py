from pytest import fixture

from sys import path

path.append(r'd:\G-Doc\TOP Academy\Python web\321\scripts\oop')

from _Cat import Cat


@fixture
def cat():
    return Cat()


def test_attrs(cat):
    # для вывода трассировки:
    # assert False
    assert cat.name and cat.color


def test_meow(cat, capsys):
    # для вывода трассировки:
    # assert False
    cat.meow()
    captured = capsys.readouterr().out.strip()
    assert captured == 'мяу'
    

def test_reproduce(cat):
    # для вывода трассировки:
    # assert False
    kittens = cat.reproduce()
    for kitty in kittens:
        assert isinstance(kitty, Cat)
    
