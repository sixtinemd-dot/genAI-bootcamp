class Animal:

    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs
        
    def sleep(self):
        return f"{self.name} is sleeping - ANIMAL"
    
class Dog(Animal):
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)
        self.trained = trained
        self.age = age
    
class Cat(Animal):
    def __init__(self, name, family, legs, friendly, house_cat):
        Animal.__init__(self, name, family, legs)
        self.friendly = friendly
        self.house_cat = house_cat


dog1 = Dog("Fluffy", "Canidae", 4, True, 5)
print(dog1.sleep())

cat1 = Cat("Mouse", "Felidae", 4, True, True)
print(cat1.friendly)

# multiple inheritence:

class Alien:

    def __init__(self, alien_name, planet):
        self.alien_name = alien_name
        self.planet = planet

class AlienDog(Alien, Dog): #order matters

    def __init__(self, alien_name, planet, name, family, legs, trained, age):
        Alien.__init__(self, alien_name, planet)
        Dog.__init__(self, name, family, legs, trained, age)


aliendog1 = AlienDog("Chubi", "Mars", "Bob", "Canidae", 6, True, 10)
print(aliendog1.planet)

# TRY EXEPT BLOC

while True:
    try:
        move = int(input("enter row and column: "))
        if move < 1 or move > 4:
            print("Please enter a number between 1 and 3")
            continue
        else:
            print("move accepted")
            break

    except Exception as e:
        print(e)

# MODULES

def sum(x, y):
    result = x + y
    return result

def sub(x, y):
    result = x - y
    return result

def mult(x, y):
    result = x * y
    return result


