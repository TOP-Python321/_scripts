class Test:
    def __init__(self):
        self.attr = 'полный доступ'
        self._private_attr = 'частный'
        self.__protected_attr = 'защищённый'

    def attributes(self):
        print(self.attr)
        print(self._private_attr)
        print(self.__protected_attr)


t1 = Test()

print(t1._private_attr)
print(t1._Test__protected_attr)

t1.attributes()
