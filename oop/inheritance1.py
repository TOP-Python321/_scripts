class A:
    """
    Родительский (базовый, над-, супер-) класс
    """
    cls_attr = 'class attribute'

    def __init__(self):
        self.inst_attr = 'instance attribute'

    def parent_method(self):
        print(self.cls_attr, self.inst_attr)


class B(A):
    """
    Дочерний (потомок, под-) класс
    """


a1 = A()
a1.new_attr = 1000

b1 = B()

# >>> A.__dict__
# mappingproxy({'__module__': '__main__', '__doc__': '\n    Родительский (базовый, над-, супер-) класс\n    ', 'cls_attr': 'class attribute', '__init__': <function A.__init__ at 0x000001BC97B95C60>, 'parent_method': <function A.parent_method at 0x000001BC97B95D00>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__annotations__': {}})
# >>>
# >>> a1.__dict__
# {'inst_attr': 'instance attribute', 'new_attr': 1000}
# >>>
# >>> a1.__dir__()
# ['inst_attr', 'new_attr', '__module__', '__doc__', 'cls_attr', '__init__', 'parent_method', '__dict__', '__weakref__', ...]
# >>>
# >>> B.__dict__
# mappingproxy({'__module__': '__main__', '__doc__': '\n    Дочерний (потомок, под-) класс\n    '})
# >>> 
# >>> b1.__dict__
# {'inst_attr': 'instance attribute'}
# >>>
# >>> b1.__dir__()
# ['inst_attr', '__module__', '__doc__', 'cls_attr', '__init__', 'parent_method', '__dict__', '__weakref__', ...]
# >>>
# >>> b1.parent_method()
# class attribute instance attribute
# >>> a1.parent_method()
# class attribute instance attribute
# >>>
# >>> b1.inst_attr = 'new value'
# >>> b1.parent_method()
# class attribute new value
# >>> a1.parent_method()
# class attribute instance attribute

