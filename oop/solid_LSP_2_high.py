"""
Liskov Substitution Principle — Принцип Подстановки Лисков

Верхний уровень
"""

import solid_LSP_2_low as model


def test_model(model_instance: model.Rectangle):
    width = model_instance.width
    model_instance.height = 10
    expected_area = width * 10
    assert expected_area == model_instance.area


rc1 = model.Rectangle(5, 8)
sq1 = model.Rectangle(5)

try:
    test_model(rc1)
except AssertionError as exc:
    print('test failed')
else:
    print('test successful')

# >>> rc1.width
# 5
# >>> rc1.height
# 10
# >>> rc1.area
# 50

try:
    test_model(sq1)
except AssertionError as exc:
    print('test failed')
else:
    print('test successful')

# >>> sq1.width
# 10
# >>> sq1.height
# 10
# >>> sq1.area
# 100
