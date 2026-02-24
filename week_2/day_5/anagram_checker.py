""" Mini-project : Anagram checker

What you will create
An anagram checker program that takes user input, validates it, and finds anagrams from a word list.

Instructions:
Download the provided text file (word list).
Create anagram_checker.py with the AnagramChecker class.
Create anagrams.py for the user interface. """

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

# Step 1: Create the AnagramChecker Class

class AnagramChecker:
    def __init__(self, words_file = "/sowpods.txt"):
        with open(dir_path + words_file, "r") as f:
            self.words = {word.strip().lower() for word in f}

    # Step 2: Implement is_valid_word Method

    def is_valid_word(self, word):
        if word in self.words:
            return True
        else:
            return False

    # Step 3: Implement is_anagram Method

    @staticmethod
    def is_anagram(word1, word2):
        sorted1 = sorted(word1.lower())
        sorted2 = sorted(word2.lower())
        if sorted1 == sorted2:
            return True
        else:
            return False

    # Step 4: Implement get_anagrams Method

    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []

        for w in self.words:
            if AnagramChecker.is_anagram(w, word) and w != word:
                anagrams.append(w)

        return anagrams
        
    







     

        
