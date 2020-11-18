# dog.py
class Dog:
    def __init__(self, name):
        self.name = name
        print("dog initialized!")

# instantiation call that creates a Dog object:
my_dog = Dog("Rex")
print(my_dog)
print(my_dog.name)