user_input = input("Please enter a 10 character string: ")

if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long")
else:
    print("Perfect string")
    first_char = user_input[0]
    last_char = user_input[9]
    print(first_char)
    print(last_char)

nothing = ""
for char in user_input:
    nothing += char
    print(nothing)

for char in range(len(user_input)):
    print(user_input[:char + 1:1])

print(user_input[0:1])
print(user_input[0:2]) 
print(user_input[0:3]) 
print(user_input[0:4]) 
print(user_input[0:5]) 
print(user_input[0:6]) 
print(user_input[0:7])
print(user_input[0:8])
print(user_input[0:9])
print(user_input[0:10]) 

import random
letters =list(user_input)
random.shuffle(letters)

shuffle = "".join(letters)
print(shuffle)
