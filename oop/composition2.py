class Employee:
    def __init__(self, name: str):
        self.name = name


class Form:
    questions: list[str] = [...]

    def __init__(self, answers: list[str]):
        self.answers = answers


class Candidate:
    def __init__(
            self,
            name: str,
            email: str,
            form: Form
    ):
        self.name = name
        self.email = email
        self.__form: Form = form
        self._interviewer: None | Employee = None

    def check_form(self) -> bool:
        ...

    def set_first_interview(self, person: Employee) -> None:
        self._interviewer = person
        ...

    def set_tech_interview(self, person: Employee) -> None:
        self._interviewer = person
        ...

    def first_interview(self) -> bool:
        ...

    def tech_interview(self) -> bool:
        ...


class HRDepartment:
    def __init__(self):
        self.employees: list[Employee] = []
        self.candidates: list[Candidate] = []

    def hire(self, person: Candidate):
        self.candidates.remove(person)
        self.employees += [
            Employee(person.name)
        ]


