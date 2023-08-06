class Person:
    # не полиморфный метод
    # @staticmethod
    # def walk():
        # print('человек идёт')
    
    # полиморфный метод
    @staticmethod
    def move():
        print('человек идёт')


class Car:
    @staticmethod
    def move():
        print('машина едет')


objects = (
    Person(), 
    Car(),
)
# без полиморфизма
# for obj in objects:
    # if isinstance(obj, Person):
        # obj.walk()
    # elif isinstance(obj, Car):
        # obj.move()

# с полиморфизмом
for obj in objects:
    obj.move()
