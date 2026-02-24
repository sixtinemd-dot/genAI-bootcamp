""" Daily challenge : Text Analysis

Instructions:
Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning. """

# Part I: Analyzing a Simple String

# Step 1: Create the Text Class
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

class Text:
    def __init__(self, text):
        self.text = text

    # Step 2: Implement word_frequency Method

    def word_frequecy(self, word):
        text_list = self.text.split()

        if word in text_list:
            return text_list.count(word)
                
        else:
            return "This word is not in the text"
            
    # Step 3: Implement most_common_word Method

    def most_common_word(self):
        word_dict = {}
        text_list = self.text.split()
        for word in text_list:
            word_count = text_list.count(word)
            word_dict[word] = word_count

        frequent_word = max(word_dict, key = word_dict.get)
        return frequent_word
    
    # Step 4: Implement unique_words Method

    def unique_words(self):
        text_list = self.text.split()
        text_set = set(text_list)
        unique_list = list(text_set)
        return unique_list
    
    # Part II: Analyzing Text from a File
    
    # Step 5: Implement from_file Class Method

    @classmethod
    def from_file(cls, file_path):
        with open(os.path.join(dir_path, file_path), 'r') as f:
            content = f.read()
            return cls(content)

text_str = Text("I love using Python and I am very good at it")

print(text_str.word_frequecy("love"))
print(text_str.word_frequecy("hate"))

print(text_str.most_common_word())

print(text_str.unique_words())

text_file = Text.from_file("daily_challenge_exemple.txt")
print(text_file.text)
         
