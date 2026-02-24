""" Instructions :
Consider this list

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
Look at this result :
{"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
You have to recreate the result using a translator module.  """

from google_trans_new import google_translator  

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

translator = google_translator()  
translated_words = []
for word in french_words:
    translated = translator.translate(word, lang_tgt='en')
    translated_words.append(translated.text)
print(translated_words)


