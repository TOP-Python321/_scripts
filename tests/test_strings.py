from pytest import mark


def upper(text: str) -> str:
    if len(text) > 15:
        raise ValueError
    else:
        return text.upper()


@mark.parametrize(
    'arg', 
    ['тестовый текст',
     'длинный тестовый текст',]
)
def test_upper(arg):
    assert upper(arg)


