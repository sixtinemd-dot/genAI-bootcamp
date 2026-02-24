""" Exercise 1: Random Sentence Generator
Goal: Create a program that generates a random sentence of a specified length from a word list.

Instructions:
Download the provided word list and save it in your development directory.
Create a function to read the words from the file.
Create a function to generate a random sentence of a given length.
Create a main function to handle user input and program flow. """

import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

# Step 1: Create the get_words_from_file function

words = []
def get_words_from_file(dir_path):
   with open(dir_path + '/words.txt', 'r') as f:
    txt_list = f.readlines()
    for word in txt_list:
      words.append(word)
    return words
   
# Step 2: Create the get_random_sentence function 

sentence_list = []
def get_random_sentence(length):
     get_words_from_file(dir_path)

     for _ in range(length):
        random_word = random.choice(words)
        sentence_list.append(random_word)
        sentence_low = [word.lower() for word in sentence_list]
        sentence_str = "".join(sentence_low)
        sentence = sentence_str.replace("\n", " ")

     return sentence

# Step 3: Create the main function

def main():
   print("This program will generate a random sentence with the number of words you wish...")
   sentence_length = input("How many words do you want in your sentence (between 1 and 20): ")
   
   if sentence_length.isdigit() == False or int(sentence_length) < 1 or int(sentence_length) > 20:
      raise TypeError("cannot use a string or a number not between 1 and 20")
   
   else:
      sentence_length_int = int(sentence_length)
      print(get_random_sentence(sentence_length_int))
      
main()
      
""" Exercise 2: Working with JSON
Goal: Access a nested key in a JSON string, add a new key, and save the modified JSON to a file. """

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

""" sampleJson["company"]["employee"]["payable"]["salary"]

sampleJson["company"]["employee"]["birth_date"] = "YYYY-MM-DD"

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/sampleJson.json', 'w') as f:
    json.dump(sampleJson, f) """

# Step 1: Load the JSON string

sample_dict = json.loads(sampleJson)

# Step 2: Access the nested “salary” key

print(sample_dict["company"]["employee"]["payable"]["salary"])

# Step 3: Add the “birth_date” key

sample_dict["company"]["employee"]["birth_date"] = "2008-06-18"

# Step 4: Save the JSON to a file

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/sampleJson.json', 'w') as f:
    json.dump(sample_dict, f, indent = 3)

