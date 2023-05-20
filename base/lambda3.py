from tkinter import Tk, Button


root = Tk()
root.geometry('300x50')


def change_title(title: str) -> None:
    """Изменяет текст заголовка главного окна."""
    root.title(title)


Button(
    root,
    text='нажми меня',
    command=lambda: change_title('new title')
).grid(
    row=0,
    column=0,
    sticky='nsew',
    padx=15,
    pady=15,
)
