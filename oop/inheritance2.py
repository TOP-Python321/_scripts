class Proteus:
    def move(self):
        pass

    def eat(self):
        pass

    def reproduce(self):
        pass


class Fish(Proteus):
    def breath(self):
        pass


class Reptiles(Fish):
    def hide(self):
        pass


class Bird(Reptiles):
    def fly(self):
        pass


class Mammals(Reptiles):
    def care(self):
        pass


class Human(Mammals):
    def speak(self):
        pass


# >>> Proteus.__mro__
# (<class '__main__.Proteus'>, <class 'object'>)
# >>>
# >>> Fish.__mro__
# (<class '__main__.Fish'>, <class '__main__.Proteus'>, <class 'object'>)
# >>>
# >>> Bird.__mro__
# (<class '__main__.Bird'>, <class '__main__.Reptiles'>, <class '__main__.Fish'>, <class '__main__.Proteus'>, <class 'object'>)
# >>>
# >>> Human.__mro__
# (<class '__main__.Human'>, <class '__main__.Mammals'>, <class '__main__.Reptiles'>, <class '__main__.Fish'>, <class '__main__.Proteus'>, <class 'object'>)
# >>>
# >>> igor = Human()
# >>> [attr for attr in igor.__dir__() if not attr.startswith('__')]
# ['speak', 'care', 'hide', 'breath', 'move', 'eat', 'reproduce']

