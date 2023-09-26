import random
#put the list countaining a lot of words
hangman_list = open('wordlist.txt').read().splitlines() # reads the file "wordlist.txt" and put it as a list
shuffled_word = random.choice(hangman_list) # take at random a word from the list
word_lenght = len(shuffled_word) # counts the lenght of the word which has been picked at random

tries = 0 # the number of total guesses from the user, starting at 0

print("\n\nThe word you are looking for is",word_lenght, "characters long\n")


def ask():
    global tries
    ask_letter = str(input("Enter a letter : ")) # asking the user to guess a leter

    if (len(ask_letter)) != 1: # looking for the input to be no more than 1 letter
        print("needs to be only one letter")
    else:
        print("idk yet")

ask()
