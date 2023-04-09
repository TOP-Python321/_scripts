immutable_object = 101
print(immutable_object)
print(f'{id(immutable_object) = }\n')

immutable_object = 102
print(immutable_object)
print(f'{id(immutable_object) = }\n')


mutable_object = [4, 2, 7, 1]
print(mutable_object)
print(f'{id(mutable_object) = }\n')

mutable_object.sort()
print(mutable_object)
print(f'{id(mutable_object) = }\n')

