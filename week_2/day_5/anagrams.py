from anagram_checker import AnagramChecker

check = AnagramChecker()

while True:
    print("Finding words anagrams program")
    print("Menu:")
    print("1. Enter a word")
    print("2. Exit")
    choice =input("Enter your choice: ")
    if not choice.isdigit():
        print("Please enter a number")
        continue
    if int(choice) != 1 and int(choice) != 2:
        print("Please enter 1 or 2")
        continue
    if int(choice) == 2:
        print("Goodbye!")
        break

    if int(choice) == 1:
        word_choice = input("Enter an english word: ").strip().lower()

        if " " in word_choice:
            print("Please enter one word only")
            continue

        if not word_choice.isalpha():
            print("Please enter word of letters...")
            continue

        if not check.is_valid_word(word_choice):
            print("Please enter a real word")
            continue

        anagrams_list = check.get_anagrams(word_choice)

        print(f"Your word : {word_choice}")
        if anagrams_list == []:
            print(f"There are no anagrams of the word {word_choice}.")
        elif len(anagrams_list) == 1:
            anagrams = "".join(anagrams_list)
            print(f"The anagram of {word_choice} is : {anagrams}.")
        else:
            anagrams = ",".join(anagrams_list)
            print(f"The anagrams of {word_choice} are : {anagrams}.")







