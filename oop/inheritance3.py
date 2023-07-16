class Vehicle:
    wheel: int = 4

    def __init__(self, average_speed: int):
        self.speed = average_speed

    def move(self):
        print(f'{self.__class__.__name__} moves with average speed {self.speed} km/h')


class Bicycle(Vehicle):
    wheel = 2


class Car(Vehicle):
    pass


class Train(Vehicle):
    wheel = 12

    def move(self):
        print(f'{self.__class__.__name__} moves along railroads with average speed {self.speed} km/h')


# пример неудачного использования наследования, потому что приходится переопределять практически все атрибуты
class Airplane(Vehicle):
    wheel = 3

    def __init__(
            self,
            average_ground_speed: int,
            average_fly_speed: int
    ):
        # Vehicle.__init__(self, average_fly_speed)
        super().__init__(average_fly_speed)
        self.speed_ground = average_ground_speed

    def move(self):
        print(f'{self.__class__.__name__} moves on the ground with average speed {self.speed_ground} km/h')

    def fly(self):
        print(f'{self.__class__.__name__} flies with average speed {self.speed} km/h')

