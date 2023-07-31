class MyError(Exception):
    def __init__(self, *paramteres: int, msg: str):
        self.params = paramteres
        self.text = msg


def func():
    a, b = 0, 1
    text = 'какой-то текст'
    ...
    raise MyError(a, b, msg=text)
    ...


try:
    func()
except MyError as exc:
    for item in exc.__dict__.items():
        print(item)
