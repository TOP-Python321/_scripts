class A:
    ...
    def method(self):
        print('метод класса A')

class B:
    ...
    def method(self):
        print('метод класса B')

class C(A, B):
    ...

class D(A):
    ...
    cls_attr = 'атрибут класса D'

    def __init__(self):
        self.attr = 125

class G:
    ...
    cls_attr = 'атрибут класса G'

class F(G, D):
    ...


# >>> C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# >>>
# >>> c = C()
# >>> c.method()
# метод класса A

# >>> F.__mro__
# (<class '__main__.F'>, <class '__main__.G'>, <class '__main__.D'>, <class '__main__.A'>, <class 'object'>)
# >>>
# >>> f = F()
# >>> f.cls_attr
# 'атрибут класса G'
# >>>
# >>> f.attr
# 125
# >>>
# >>> f.method()
# метод класса A

