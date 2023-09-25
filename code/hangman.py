import random
#put the list countaining a lot of words
hangman_list = open('wordlist.txt').read().splitlines()
shuffled_word = random.choice(hangman_list)

word_lenght = len(shuffled_word)

print("The word you are looking for is",word_lenght, "characters long")

def ask():
    ask_letter = str(input("Enter a letter : "))

ask()
