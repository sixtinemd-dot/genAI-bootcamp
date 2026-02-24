""" Exercise 1: Currencies
Goal: Implement dunder methods for a Currency class to handle string representation, integer conversion, addition, and in-place addition. """

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #Your code starts HERE

    def __str__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"

    def __repr__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):

        if isinstance(other, int):
            return self.amount + other
        
        if type(other) != int:
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")

    def __iadd__(self, other):

        if isinstance(other, int):
            self.amount += other
            return self
        
        if isinstance(other, Currency):
            if self.currency == other.currency: 
                self.amount += other.amount
                return self
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

# print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>

""" Exercise 2: Import
Goal: Create a module with a function and import it into another file.

Instructions:
Create a func.py file with a function that sums two numbers and prints the result. Then, import and call the function from exercise_one.py.
 """

""" Exercise 3: String module
Goal: Generate a random string of length 5 using the string module.

Instructions:
Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only. """

import string
import random

random_string = "".join(random.choice(string.ascii_letters) for _ in range(5)) 
print(random_string)

""" Exercise 4: Current Date
Goal: Create a function that displays the current date. """

from datetime import date

today = date.today()
print(today)

""" Exercise 5: Amount of time left until January 1st
Goal: Create a function that displays the amount of time left until January 1st. """

import datetime

current_date = datetime.datetime.today()
january_date = datetime.datetime(2026, 1, 1, 00, 00, 00)

time_dif = january_date - current_date
print(f"There is this much time lest until january 1st: {time_dif} !")

""" Exercise 6: Birthday and minutes

Instructions:
Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.
 """

import datetime 

def birthday(birthdate_str):
    current_date = datetime.datetime.today()
    format_string = "%d/%m/%Y %H:%M:%S"
    birthdate = datetime.datetime.strptime(birthdate_str, format_string)
    date_dif = current_date - birthdate
    seconds_lived = date_dif.total_seconds()
    print(f"You have lived {seconds_lived} seconds in your life!")

birthday("18/6/2008 08:00:00")

""" Exercise 7: Faker Module
Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.
Read more about this module HERE

Instructions:
Install the faker module and use it to create a list of dictionaries, where each dictionary represents a user with fake data. """

from faker import Faker
faker = Faker() 

users = []

def add_user(users_number):
    number = int(users_number)
    for _ in range(number):
        
        user_dict = {"name": faker.name(), "address": faker.address(), "language_code": faker.language_code()}
        users.append(user_dict)

add_user(6)
print(users)



