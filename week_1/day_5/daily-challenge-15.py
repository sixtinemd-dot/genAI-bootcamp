""" Challenge 1: Sorting

Instructions:
Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted words also separated by commas. """

input_words = input("Enter words separated by commas: ")

def sort_words(words):

    word_list = words.split(",") 
    word_list.sort()            
    result = ",".join(word_list)
    print(result)

sort_words(input_words)

""" Challenge 2: Longest Word

Instructions:
Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word. """

input_sentence = input("Enter a sentence: ")

def longest_word(sentence):
    sentence_words = sentence.split(" ")
    longest = ""
    for word in sentence_words:
        if len(word) > len(longest):
            longest = word
    print(f"The longest word is {longest}")

longest_word(input_sentence)