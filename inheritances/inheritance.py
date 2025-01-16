
class Animal:
    def __init__(self, name):
        if name is None or name == "":
            raise ValueError("Name cannot be None or empty")
        self.name = name
        self.age = None

    def eat(self, food):
        print(f"{self.name} eats {food}")

    def set_age(self, age):
        if age is None:
            self.age = 0
        elif age < 0:
            raise ValueError("Age cannot be negative")
        else:
            self.age = age

    def get_age(self):
        if self.age is None:
            raise ValueError("Age has not been set")
        else:
            return self.age

    def __str__(self):
        return f"I'm {self.name} and {self.age} years old"


class Dog(Animal):
    valid_breeds = ["Bulldog", "Golden Retriever", "German Shepherd"]

    def __init__(self, name, breed):
        super().__init__(name)
        if breed not in Dog.valid_breeds:
            self.breed = "Unknown"
        else:
            self.breed = breed

    def bark(self):
        print(f"{self.name} barks and is of breed: {self.breed}")

    def __str__(self):
        return super().__str__() + f" and are of breed {self.breed}"


if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    # animal = Animal("")  # ValueError: Name cannot be None or empty
    animal = Animal("Chicken")

    dog.eat("meat")
    dog.bark()

    # print(dog.get_age())  # ValueError: Age has not been set
    # dog.set_age(-5)  # ValueError: Age cannot be negative

    age_str = input("What is the dog's age? : ")
    try:
        age = int(age_str)
        dog.set_age(age)
    except ValueError:
        print("Invalid age. Setting age to 0.")
        dog.set_age(0)

    # dog.set_age(10)
    print("Dog age:", dog.get_age())

    animal.eat("corn")

    print(dog)
    print(animal)

    # print(dog.name)
    # print(dog.breed)
    # print(dog.__class__.__name__)
    #
    # print(animal.name)
    # print(animal.__class__.__name__)

    # print(isinstance(dog, Animal))      # True
    # print(isinstance(dog, Dog))         # True
    # print(isinstance(dog, object))      # True
    #
    # print(isinstance(animal, Animal))   # True
    # print(isinstance(animal, Dog))      # False
    # print(isinstance(animal, object))   # True
    #
    # print(issubclass(Dog, Animal))      # True
    # print(issubclass(Animal, Dog))      # False
    # print(issubclass(Dog, object))      # True
    # print(issubclass(Animal, object))   # True
