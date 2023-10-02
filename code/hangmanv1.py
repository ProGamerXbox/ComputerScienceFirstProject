import random
#put the list countaining a lot of words
hangman_list = open('wordlist.txt').read().splitlines() # reads the file "wordlist.txt" and put it as a list
shuffled_word = random.choice(hangman_list) # take at random a word from the list
word_lenght = len(shuffled_word) # counts the lenght of the word which has been picked at random
index = 1
tries = 7
emptylist = []

print("\n\nThe word you are looking for is",word_lenght, "characters long\n")

print("\n",shuffled_word)

ask_letter = input("Enter a letter : ")

emptylist.append(ask_letter)
print(emptylist)


while tries != 0:

    if (len(ask_letter)) >= 1: # looking for the input to be no more than 1 letter
        print("needs to be only one letter")

    if ask_letter in shuffled_word:
        emptylist.append(ask_letter)
        print("ITS IN THE WORD!!!")
        print(emptylist)
        ask_letter = input("Enter a letter : ")

    else:
        emptylist.append(ask_letter)
        tries -= 1
        print("That isn't in the word! You lost a guess!")
        print(emptylist)
        print("you now have", tries, "attempts remaining")
        ask_letter = input("Enter a letter : ")
        
