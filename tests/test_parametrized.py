from pytest import mark

from sys import path

path.append(r'd:\G-Doc\TOP Academy\Python web\321\scripts\base')
path.append(r'd:\G-Doc\TOP Academy\Python web\321\scripts\oop')

from function4 import pos_or_neg_or_zero
from func_args1 import div


@mark.parametrize('number_for_test', [-1, 0, 1])
def test_pos_or_neg_or_zero(number_for_test):
    result = pos_or_neg_or_zero(number_for_test)
    assert result is not None
    # неэффективное использование параметризации
    # if number_for_test < 0:
    #     assert result == 'непонятно что'
    # elif number_for_test == 0:
    #     assert result == 'ноль'
    # elif number_for_test > 0:
    #     assert result == 'положительное'


@mark.parametrize('number1,number2', [(5, 2), (3, 10), (2, 0)])
def test_div1(number1, number2):
    result = div(number1, number2)
    assert result is not None


@mark.parametrize('number2', [3, 0.3, 0])
@mark.parametrize('number1', [-10, 0, 10])
def test_div2(number1, number2):
    result = div(number1, number2)
    assert result is not None


