""" exercice 1:
Print the following output using one line of code:
Instructions
Hello world
Hello world
Hello world
Hello world
 """

sentence = "Hello world\n"
print(sentence * 4)

""" Exercise 2: Some Math
Instructions
Write code that calculates the result of:

(99^3)*8 (meaning 99 to the power of 3, times 8). """

result = 99**3*8
print(result)

""" Exercise 3: What is the output?
Instructions
Predict the output of the following code snippets:
Coment what is your guess, then run the code and compare

Example:
>>> 15 < 8 #False
 """

"""
>>> 5 < 3 #False
>>> 3 == 3 #True
>>> 3 == "3" #False
>>> "3" > 3 #False
>>> "Hello" == "hello" #False
 """

""" Exercise 4: Your computer brand
Instructions
Create a variable called computer_brand which value is the brand name of your computer.
Using the computer_brand variable, print a sentence that states the following:
"I have a <computer_brand> computer." """

computer_brand = "MacBook"
print(f"I have a {computer_brand} computer.")

""" Exercise 5: Your information
Instructions
Create a variable called name, and set it’s value to your name.
Create a variable called age, and set it’s value to your age.
Create a variable called shoe_size, and set it’s value to your shoe size.
Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
Have your code print the info message.
Run your code.
 """

my_name = "Sixtine"
age = "17"
shoe_size = "40"
info = f"Hi, my name is {my_name}, I'm {age} years old and I wear a size {shoe_size} shoe"
print(info)

""" Exercise 6: A & B
Instructions
Create two variables, a and b.
Each variable’s value should be a number.
If a is bigger than b, have your code print "Hello World". """

a = 16
b = 5
if a > b:
    print("Hello World")

""" Exercise 7: Odd or Even
Instructions
Write code that asks the user for a number and determines whether this number is odd or even. """

number = input("enter a number: ")
number_ = int(number)
if number_ % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

""" Exercise 8: What’s your name?
Instructions
Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
 """

user_name = input("What is your name? ")
if user_name == my_name:
    print("We have the same name!")

else:
    print("your name sucks :)")

""" Exercise 9: Tall enough to ride a roller coaster
Instructions
Write code that will ask the user for their height in centimeters.
If they are over 145 cm, print a message that states they are tall enough to ride.
If they are not tall enough, print a message that says they need to grow some more to ride. """

user_height = input("Please enter your heigt in cm: ")
user_height_int = int(user_height)
if user_height_int > 145:
    print("You are tall enough to ride!")
else:
    print("Sorry, You'll have to grow some more before going on this ride...")

#Exercice XP gold:
""" Exercise 1 : Hello World-I love Python
Instructions
Print the following output in one line of code:
Hello world
Hello world
Hello world
Hello world
I love python
I love python
I love python
I love python """

print("Hello world\n"*4+"I love python\n"*4)

""" Exercise 2 : What is the Season ?
Instructions
Ask the user to input a month (1 to 12).
Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2) """

month = input("Enter a month in number (1-12): ")
month_ = int(month)
if 5 >= month_ >= 3 :
    print("this month is in spring")
elif 8 >= month_ >= 6 :
    print("this month is in summer")
elif 11 >= month_ >= 9 :
    print("this month is in autumn")
else : 
    print("this month is in winter")
     