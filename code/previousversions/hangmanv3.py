import random
#put the list countaining a lot of words
hangman_list = open('wordlist.txt').read().splitlines() # reads the file "wordlist.txt" and put it as a list
shuffled_word = random.choice(hangman_list) # take at random a word from the list
word_lenght = len(shuffled_word) # counts the lenght of the word which has been picked at random
index = 1
tries = 7
emptylist = []

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def hangmanascii():
    global tries
    global HANGMANPICS
    
    if tries == 6:
        print(HANGMANPICS[0])
    if tries == 5:
        print(HANGMANPICS[1])
    if tries == 4:
        print(HANGMANPICS[2])
    if tries == 3:
        print(HANGMANPICS[3])
    if tries == 2:
        print(HANGMANPICS[4])
    if tries == 1:
        print(HANGMANPICS[5])
    if tries <= 0:
        print(HANGMANPICS[6])
def lose():
    global shuffled_word
    print('You lost')
    print('the word was',"'", shuffled_word, "'")
    exit()

print("""
  _    _          _   _  _____ __  __          _   _ 
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|__|_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
  / ____|   /\   |  \/  |  ____|                   
 | |  __   /  \  | \  / | |__    Made by :                    
 | | |_ | / /\ \ | |\/| |  __|        - Tom           
 | |__| |/ ____ \| |  | | |____       - William          
  \_____/_/    \_\_|  |_|______|      - Marius    
""")

print("\nThe word you are looking for is",word_lenght, "characters long")

print("\n",shuffled_word)

ask_letter = input("""
-----------------------
Guess a letter : """)

while tries > 1:

    if (len(ask_letter)) > 1: # looking for the input to be no more than 1 letter
        hangmanascii()
        print("/!\ Your guess needs to be only one letter /!\ ")
        ask_letter = input("""
-----------------------
Guess a letter : """)
        continue

    if ask_letter in shuffled_word:
        hangmanascii()
        print("[✔]'",ask_letter,"'", "is in the word !")
        print("\n[-] Wrong letters guessed :", emptylist)
        ask_letter = input("""
-----------------------
\nGuess a letter : """)

    else:
        tries -= 1
        emptylist.append(ask_letter)
        hangmanascii()
        print("\n[!] Letter not in the word! You lost a guess!")
        print("\nWrong letters guessed :", emptylist)
        print("[!] You now have", tries, "attempts remaining")
        ask_letter = input("""
-----------------------
\nGuess a letter : """)

else:
    lose()