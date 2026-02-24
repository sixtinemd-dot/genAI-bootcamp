""" Exercise 1: Cats

Instructions:
Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details. """

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
    
    def find_oldest_cat(cat1, cat2, cat3):
        oldest = cat1
        if cat2.age > oldest.age:
            oldest = cat2
        
        if cat3.age > oldest.age:
            oldest = cat3

        return oldest

cat1 = Cat("Metuka", 11)
cat2 = Cat("Milwaukee", 16)
cat3 = Cat("Toulouse", 5)

oldest_cat = Cat.find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

""" Exercise 2 : Dogs
Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.

Instructions:
Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes. """

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def identity(self):
        print(f"{self.name} = {self.height}")
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        print(f"{self.name} jumps {self.height *2} cm high!")

    def find_tallest_dog(dog1, dog2):
        if dog1.height > dog2.height:
            print(f"{dog1.name} is taller than {dog2.name}")
        else:
            print(f"{dog2.name} is taller than {dog1.name}")

davids_dog = Dog("Max", 80)
sarahs_dog = Dog("Luna", 23)

davids_dog.identity()
sarahs_dog.identity()

davids_dog.bark()
sarahs_dog.bark()

davids_dog.jump()
sarahs_dog.jump()

Dog.find_tallest_dog(davids_dog, sarahs_dog)

""" Exercise 3 : Who’s the song producer?
Goal: Create a Song class to represent song lyrics and print them.

Instructions:
Create a Song class with a method to print song lyrics line by line. """

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)

another_day = Song(["Oh, think twice", "'cause it's another day for you,", "you and me in paradise"])

another_day.sing_me_a_song()

""" Exercise 4 : Afternoon at the Zoo
Goal:

Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.
 """

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, *new_animal):
        if new_animal:
            for each_animal in new_animal:
                if each_animal not in self.animals:
                    self.animals.append(each_animal)
                else:
                    print(f"{each_animal} allready exists in the zoo")
        print(", ".join(self.animals))

    def get_animals(self):
        print(", ".join(self.animals))

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            pass

    def sort_animals(self):
        self.animals.sort()
        self.first_letter = {}
        for value in self.animals:
            if value[0] not in self.first_letter.keys():
                self.first_letter[value[0]] = [value]
            else:
               self.first_letter[value[0]].append(value) 

        print(self.first_letter)

    def get_groups(self):
        for value in self.first_letter.values():
            if value[-1] == value[0]:
                pass
            else:
                print(value)

Pairidaiza = Zoo("Pairidaiza")

Pairidaiza.add_animal("Giraffe", "Bear", "Baboon")
Pairidaiza.add_animal("Bear")
Pairidaiza.add_animal("Baboon")
Pairidaiza.add_animal("Cat")
Pairidaiza.add_animal("Cougar")
Pairidaiza.get_animals()
Pairidaiza.sell_animal("Bear")
Pairidaiza.get_animals()
Pairidaiza.sort_animals()
Pairidaiza.get_groups()


