class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
    
    @property
    def login(self) -> str:
        return self.__login
    
    @login.setter
    def login(self, new_login: str):
        self.__login = new_login.lower()
    
    @property
    def password(self):
        # raise NotImplementedError
        return None
    
    @password.setter
    def password(self, new_password: str):
        self.__password = hash(new_password)
    
    def autenthicate(self, login: str, password: str):
        if login == self.login:
            if hash(password) == self.__password:
                print('авторизован')
            else:
                print('неверный пароль')
        else:
            print('неверный логин')


user1 = User('UsEr', 'qwerty5')

# >>> user1.__login
# AttributeError: 'User' object has no attribute '__login'. Did you mean: 'login'?
# >>>
# >>> user1.password
# >>> user1.__password
# AttributeError: 'User' object has no attribute '__password'. Did you mean: 'password'?
# >>>
# >>> user1.__dict__
# {'_User__login': 'user', '_User__password': 4013990443963360952}
# >>>
# >>> user1._User__password
# 4013990443963360952

