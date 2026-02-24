""" Exercise 1: Pets

Instructions:
Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
See the example below, before diving in. """

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"
    
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def __init__(self, name, age, eyes):
        super().__init__(name, age)
        self.eyes = eyes

bengalcat = Bengal("Juliette", 16)
chartreuxcat = Chartreux("Metuka", 10)
siamesecat = Siamese("Leo", 2, "blue")

all_cats = [bengalcat, chartreuxcat, siamesecat]

sara_pets = Pets(all_cats)
sara_pets.walk()

""" Exercise 2: Dogs
Goal: Create a Dog class with methods for barking, running speed, and fighting. """

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        result = self.weight / self.age * 10
        return result 
    
    def fight(self, other_dog):
        self.run_speed()
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} wins the fight"
        else:
            return f"{other_dog.name} wins the fight"
        
dog1 = Dog("Jazz", 14, 60)
dog2 = Dog("Ginger", 9, 87)
dog3 = Dog("Farofa", 3, 20)
        
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())
print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))

""" Exercise 3: Dogs Domesticated
Goal: Create a PetDog class that inherits from Dog and adds training and tricks. """
# ==> see file exercice_3_XP_22.py

""" Exercise 4: Family and Person Classes
Goal:
Practice working with classes and object interactions by modeling a family and its members. """

class Person:
    def __init__(self, first_name, age,):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False
        

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

    def family_presentation(self):
        print(f"Family {self.last_name}: ")
        for member in self.members:
            print(f"{member.first_name} {self.last_name}")


person1 = Family("Mauchard")
person1.born("Sixtine", 17)
person1.check_majority("Sixtine")
person1.family_presentation()


        








