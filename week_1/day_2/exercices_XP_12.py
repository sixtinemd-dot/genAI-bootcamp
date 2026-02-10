""" Exercise 1: Favorite Numbers

Instructions:

Create a set called my_fav_numbers and populate it with your favorite numbers.
Add two new numbers to the set.
Remove the last number you added to the set.
Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
Note: Sets are unordered collections, so ensure no duplicate numbers are added. """

my_fav_numbers = set([1,2,16,18])
my_fav_numbers.add(17)
my_fav_numbers.add(5)
print(my_fav_numbers)
my_fav_numbers.remove(5)
print(my_fav_numbers)

friend_fav_numbers = set([1,4,20,7])
print(friend_fav_numbers)

our_fav_numbers = set(my_fav_numbers.union(friend_fav_numbers))
print(our_fav_numbers)

""" Exercise 2: Tuple

Instructions:

Given a tuple of integers, try to add more integers to the tuple.
Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple. """

a_tuple = (1,3,5,76)
print(a_tuple)
# Tuples are immutable, there is no way possible to add an element to it

""" Exercise 3: List Manipulation
Key Python Topics:

Instructions:

You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
Remove "Banana" from the list.
Remove "Blueberries" from the list.
Add "Kiwi" to the end of the list.
Add "Apples" to the beginning of the list.
Count how many times "Apples" appear in the list.
Empty the list.
Print the final state of the list.
 """

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
print(basket)

basket.pop(-1)
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0,"Apples")
print(basket)

basket_count=basket.count("Apples")
print(basket_count)

basket.clear()
print(basket)

""" Exercise 4: Floats

Instructions:

Recap: What is a float? What’s the difference between a float and an integer?
Create a list containing the following sequence of mixed types: floats and integers:
1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
Avoid hard-coding each number manually.
Think: Can you generate this sequence using a loop or another method?
 """

# A float is a decimal number, the difference with integers is because integers are whole numbers.

start = 1
numbers = []
while start <=4.5 :
    start += 0.5
    numbers.append(start)

print(numbers)

""" Exercise 5: For Loop

Instructions:

Write a for loop to print all numbers from 1 to 20, inclusive.
Write another for loop that prints every number from 1 to 20 where the index is even. """

for number in range(1,21):
    print(number)

for number in range(1,21,2):
    print(number)

""" Exercise 6: While Loop

Instructions:

Use an input to ask the user to enter their name.
Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
hint: check for the method isdigit()
if the input is incorrect, keep asking for the correct input until it is correct
if the input is correct print “thank you” and break the loop """

name = input("Enter your name: ")
while name.isdigit() or len(name) < 3:
    print("incorrect")
    name = input("give the coreect name: ")
print("Thank you")

""" Exercise 7: Favorite Fruits

Instructions:

Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
Store these fruits in a list.
Ask the user to input the name of any fruit.
If the fruit is in their list of favorite fruits, print:
"You chose one of your favorite fruits! Enjoy!"
If not, print:
"You chose a new fruit. I hope you enjoy it!" """

fav_fruit = input("Enter your favorite fruits (you can put multiple separeted by spaces): ")
fav_fruit_list = fav_fruit.split()

fruit = input("Name any fruit: ")
if fruit in fav_fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

""" Exercise 8: Pizza Toppings

Instructions:

Write a loop that asks the user to enter pizza toppings one by one.
Stop the loop when the user types 'quit'.
For each topping entered, print:
"Adding [topping] to your pizza."
After exiting the loop, print all the toppings and the total cost of the pizza.
The base price is $10, and each topping adds $2.50.
 """

topping =input("Enter a pizza topping. Type 'quit' if you want to stop: ")
toppings = []
cost = 10
while topping != 'quit':
    print(f"Adding {topping} to your pizza.")
    toppings.append(topping)
    cost += 2.50
    topping =input("Enter another pizza topping. Type 'quit' if you want to stop: ")

print(toppings)
print(cost)

""" Exercise 9: Cinemax Tickets

Instructions:

Ask for the age of each person in a family who wants to buy a movie ticket.
Calculate the total cost based on the following rules:
Free for people under 3.
$10 for people aged 3 to 12.
$15 for anyone over 12.
Print the total ticket cost. """

people = input("One ticket per person. How many are you buying? ")
people_int = int(people)
cost = 0

for i in range(people_int):
    age = input(f"Enter the age of person n°{i + 1}: ")
    age_int = int(age)
    if age_int < 3:
        cost += 0
    elif 3 <= age_int <= 12:
        cost += 10
    else:
        cost += 15

total_cost = input(f"the total cost of the tickets is {cost}$.")  
