class Group(list):
    def __init__(self, teacher: str):
        super().__init__()
        self.teacher = teacher

    def __str__(self):
        return f"{self.teacher}: {', '.join(self)}"


py321 = Group('Геннадий')
