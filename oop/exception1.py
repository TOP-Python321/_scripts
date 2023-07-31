message = 'текст ошибки'


class MyError(Exception):
    def __init__(self):
        super().__init__(message)


raise MyError

# вызовет TypeError:
# raise MyError('asdasd')

