class DictOfRanges(dict):
    """
    Словарь диапазонов: при обращении по int ключу возвращает значение, соответствующее кортежу, в диапазон которого попадает ключ.

    self: dict[tuple[int, int], Any]
    """
    def __init__(self, kwargs):
        try:
            for left, right in kwargs:
                if not isinstance(left, int) or not isinstance(right, int):
                    raise ValueError(f'keys for {self.__class__.__name__!r} must be (int, int) objects')
        except TypeError:
            raise ValueError(f'keys for {self.__class__.__name__!r} must be (int, int) objects')
        super().__init__(kwargs)

    def __getitem__(self, item: int):
        if isinstance(item, int):
            for left, right in self:
                if left <= item < right:
                    return super().__getitem__((left, right))
        else:
            raise TypeError


health = DictOfRanges({
    (0, 10): 'при смерти',
    (10, 35): 'тяжело ранен',
    (35, 80): 'ранен',
    (80, 100): 'здоров',
    # ('a', 'b'): 'здоров',
})
