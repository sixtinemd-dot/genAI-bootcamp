# Exercise 1: Converting Lists into Dictionaries

"""instructions
You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

Lists:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

Expected Output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30} """

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys, values))
print(dictionary)

# Exercise 2: Cinemax #2

""" instructions
Write a program that calculates the total cost of movie tickets for a family based on their ages.

Family members’ ages are stored in a dictionary.
The ticket pricing rules are as follows:
Under 3 years old: Free
3 to 12 years old: $10
Over 12 years old: $15

Family Data:
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

Loop through the family dictionary to calculate the total cost.
Print the ticket price for each family member.
Print the total cost at the end.

Bonus:
Allow the user to input family members’ names and ages, then calculate the total ticket cost. """

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0


for name, age in family.items():
    if age < 3:
        cost = 0
        print(f"{name.title()} = {cost}$")
        total_cost += cost 
    elif 3 <= age <= 12:
        cost = 10
        print(f"{name.title()} = {cost}$")
        total_cost += cost 
    else:
        cost = 15
        print(f"{name.title()} = {cost}$")
        total_cost += cost 

print(f"The total cost is {total_cost}$")

# Exercise 3: Zara

""" Instructions
Create and manipulate a dictionary that contains information about the Zara brand.

Brand Information:
name: Zara
creation_date: 1975
creator_name: Amancio Ortega Gaona
type_of_clothes: men, women, children, home
international_competitors: Gap, H&M, Benetton
number_stores: 7000
major_color: 
    France: blue, 
    Spain: red, 
    US: pink, green """

# Create a dictionary called brand with the provided data.
brand = { "name" : "Zara",
"creation_date" : "1975",
"creator_name" : "Amancio Ortega Gaona",
"type_of_clothes" : ["men", "women", "children", "home"],
"international_competitors" : ["Gap", "H&M", "Benetton"],
"number_stores" : 7000,
"major_color" : {"France" : "blue", 
                 "Spain" : "red", 
                 "US": ["pink", "green"]}}

print(brand)
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
brand["number_stores"] = 2
# Print a sentence describing Zara’s clients using the type_of_clothes key.
print(f"Zara sells different things in multiple sectors, such as {brand["type_of_clothes"]}.")
# Add a new key country_creation with the value Spain.
brand["country_creation"] = "Spain"
# Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in brand.keys():
    brand["international_competitors"].append("Desigual")

# Delete the creation_date key.
del brand["creation_date"]
# Print the last item in international_competitors.
print(brand["international_competitors"][-1])
# Print the major colors in the US.
print(brand["major_color"]["US"])
# Print the number of keys in the dictionary.
print(len(brand.keys()))
# Print all keys of the dictionary.
# print(brand.keys())
for key in brand.keys():
    print(key)

""" Bonus:
Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result. """


# Exercise 4: Disney Characters

""" Instructions
You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:

Character List:
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

Expected Results:
1. Create a dictionary that maps characters to their indices:
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

2. Create a dictionary that maps indices to characters:
{0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4} """

# 1
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_dict1 = {}

for index, char in enumerate(users):
    disney_dict1[char] = index
print(disney_dict1)

#2
disney_dict2 = {}
for index, char in enumerate(users):
    disney_dict2[index] = char
print(disney_dict2)

#3
disney_dict3 = {}
users_sorted = sorted(users)
for index, char in enumerate(users_sorted):
    disney_dict3[char] = index
print(disney_dict3)



