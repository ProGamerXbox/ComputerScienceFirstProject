import random
#put the list countaining a lot of words
hangman_list = open('wordlist.txt').read().splitlines() # reads the file "wordlist.txt" and put it as a list
shuffled_word = random.choice(hangman_list) # take at random a word from the list
word_lenght = len(shuffled_word) # counts the lenght of the word which has been picked at random
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
tries = 1
wrongguessedword = []

hintguesses = ''

for x in shuffled_word:
    hintguesses = hintguesses + '_'
hintguesses = list(hintguesses)
letterLength = 0

print("".join(hintguesses))


HANGMANPICS = ['','''
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
    print(HANGMANPICS[tries])
def lose():
    global shuffled_word
    print('\nYou lost')
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

ask_letter = input("\n-----------------------\nGuess a letter : ")

while tries <= 7:
    print(tries)

    if('_' not in "".join(hintguesses)):
        print("\nYou won yeay !")
        exit()

    if (len(ask_letter)) > 1: # looking for the input to be no more than 1 letter
        print("/!\ Your guess must only be one letter /!\ ")
        ask_letter = input("\n-----------------------\nGuess a letter : ")
        print("\n","".join(hintguesses))
        continue

    elif ask_letter in alphabet:

        if ask_letter in shuffled_word:
            hangmanascii()
            print("[✔]'",ask_letter,"'", "is in the word !")
            print("\n[-] Wrong letters guessed :", wrongguessedword)
            print("\n","".join(hintguesses))
            ask_letter = input("\n-----------------------\nGuess a letter : ")

        else:
            tries += 1
            print(tries)
            wrongguessedword.append(ask_letter)
            hangmanascii()
            print("\n[!] Letter not in the word! You lost a guess!")
            print("\nWrong letters guessed :", wrongguessedword)
            print("[!] You now have", 8-tries, "attempts remaining")
            print("\n","".join(hintguesses))
            
            if(8-tries == 0):
                lose()

            ask_letter = input("\n-----------------------\nGuess a letter : ")
            if ask_letter in wrongguessedword:
                tries -= 1
                print("You already guessed this letter")   
                wrongguessedword.remove(ask_letter)
                print("\n","".join(hintguesses))

            for x in shuffled_word:
              if(x==ask_letter):
                hintguesses[shuffled_word.find(ask_letter, letterLength)] = ask_letter
                letterLength = shuffled_word.find(ask_letter, letterLength) +1

    else:
        print("[!] The letter guessed must be between [a-z]")
        print("\n","".join(hintguesses))
        ask_letter = input("\n-----------------------\nGuess a letter : ")
else:
    lose()