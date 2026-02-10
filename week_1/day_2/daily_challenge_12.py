""" Challenge 1: Multiples of a Number

Instructions:
1. Ask the user for two inputs:
A number (integer).
A length (integer).

2. Create a program that generates a list of multiples of the given number.
3. The list should stop when it reaches the length specified by the user. """

number_ = input("please enter a number: ")
length_ = input("how many multpilier of this number do you want? ")
number = int(number_)
length = int(length_)

i = 1
multiplier = []
number__ = 0

while i <= length:
    number__ += number
    i += 1
    multiplier.append(number__)

print(multiplier)

""" Challenge 2: Remove Consecutive Duplicate Letters

Instructions:
1. Ask the user for a string.
2. Write a program that processes the string to remove consecutive duplicate letters.

The new string should only contain unique consecutive letters.
For example, “ppoeemm” should become “poem” (removes consecutive duplicates like 'pp’, 'ee’, and 'mm’).
3. The program should print the modified string. """

string = input("Please enter a string: ")

new_string = ""

for char in string:
    if not new_string or char != new_string[-1]:
        new_string += char

print(new_string)


