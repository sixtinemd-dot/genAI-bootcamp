# decaorators

import re 
import datetime

special_chars = ["!", "@", "$"]

class Person:

    def __init__(self, first_name, last_name, birth_date):
        self.first_name = self.format_name(first_name)
        self.last_name = self.format_name(last_name)
        self.birth_date = birth_date
        self._full_name = None # PROTECTED (just for internal use) because the attribute is in @property 
        self.__salary = 35000 # PRIVATE

    @staticmethod #static method (usually called inside the class), a method w/o self (usually for internal formating or ogranization)
    def format_name(name): 
        name = name.strip().capitalize()
        name = re.sub(r'[^a-zA-Z]', '', name)
        return name
    
    @classmethod
    #class method, class level (class instead of self)
    def from_age(cls, first_name, last_name, age):
        current_year = datetime.datetime.today().year
        birth_year = current_year - age
        birth_date = f"1-1-{birth_year}"
        return cls(first_name, last_name, birth_date)
    
    @property #related to encapsulation
    def full_name(self):
        self._full_name = f"{self.first_name} {self.last_name}" #new attribute
        return self._full_name
    
    @full_name.setter #there are other options (getter, deleter,...)
    def full_name(self):
        self._full_name = f"{self.first_name} {self.last_name}"

    def presentation(self):
        print(f"Hello, my name is {self.full_name}")

    #donder methods AKA magic methods

    def __str__(self): #supposed to show everytime we print an object
        return f"Hello, my name is {self.full_name}, my birth-date is {self.birth_date}"
    
    def __repr__(self): #if no str is will print the repr. order doesn't matter but the first one should be these 2
        return f"{self.__dict__}"


p1 = Person("John", "Snow&", "05-12-1980")
p2 = Person("Aria", "STARK5", "30-07-2000")
print(p1.first_name, p2.last_name)
print(p2.first_name, p2.last_name)

print(p1)

# creazting an pbject using our classmethod

p3 = Person.from_age("Sansa", "Stark", 30)
print(p3.birth_date)

# create a static method that format the first_name and last_name as full_name 
# create an internal attribute called full_name and do it with the static method 
# create p4 name Daenerys Targaryen, age 32
# print daenerys full name

p4 = Person("Daenerys", "Targaryen", 32)
print(p4.full_name)
#print(p4.salary) PRIVATE
#print(p4.__salary) PRIVATE
print(p2._Person__salary) #non traditional way of accessing a private attribute/property

p2.presentation()
