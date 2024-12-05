
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} eats {food}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks")


if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    animal = Animal("Animal")

    dog.eat("meat")
    dog.bark()

    animal.eat("grass")

    print(dog.name)
    print(dog.breed)
    print(dog.__class__.__name__)

    print(animal.name)
    print(animal.__class__.__name__)

    print(isinstance(dog, Animal))      # True
    print(isinstance(dog, Dog))         # True
    print(isinstance(dog, object))      # True

    print(isinstance(animal, Animal))   # True
    print(isinstance(animal, Dog))      # False
    print(isinstance(animal, object))   # True

    print(issubclass(Dog, Animal))      # True
    print(issubclass(Animal, Dog))      # False
    print(issubclass(Dog, object))      # True
    print(issubclass(Animal, object))   # True
