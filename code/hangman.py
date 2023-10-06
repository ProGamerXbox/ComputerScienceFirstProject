import random
#put the list countaining a lot of words
hangman_list = open('wordlist.txt').read().splitlines() # reads the file "wordlist.txt" and put it as a list
shuffled_word = random.choice(hangman_list) # take at random a word from the list
word_lenght = len(shuffled_word) # counts the lenght of the word which has been picked at random
alphabet = open('alphabet.txt').read().splitlines()
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
    print('''
 _______  _______  __   __  _______  
|       ||   _   ||  |_|  ||       | 
|    ___||  |_|  ||       ||    ___| 
|   | __ |       ||       ||   |___  
|   ||  ||       ||       ||    ___| 
|   |_| ||   _   || ||_|| ||   |___  
|_______||__| |__||_|   |_||_______| 
 _______  __   __  _______  ______   
|       ||  | |  ||       ||    _ |  
|   _   ||  |_|  ||    ___||   | ||  
|  | |  ||       ||   |___ |   |_||_ 
|  |_|  ||       ||    ___||    __  |
|       | |     | |   |___ |   |  | |
|_______|  |___|  |_______||___|  |_|

''')
    print('\nthe word was',"'", shuffled_word, "'\n")
    exit()
def win():
    print('''
 __   __  _______  __   __      
|  | |  ||       ||  | |  |     
|  |_|  ||   _   ||  | |  |     
|       ||  | |  ||  |_|  |     
|_     _||  |_|  ||       |     
  |   |  |       ||       |     
  |___|  |_______||_______|     
 _     _  _______  __    _  __  
| | _ | ||       ||  |  | ||  | 
| || || ||   _   ||   |_| ||  | 
|       ||  | |  ||       ||  | 
|       ||  |_|  ||  _    ||__| 
|   _   ||       || | |   | __  
|__| |__||_______||_|  |__||__| 
''')
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

#print("\n",shuffled_word)

ask_letter = input("\n-----------------------\nGuess a letter : ")

while tries <= 7:

    if('_' not in "".join(hintguesses)):
        win()

    if (len(ask_letter)) > 1: # looking for the input to be no more than 1 letter
        print("/!\ Your guess must only be one letter /!\ ")
        ask_letter = input("\n-----------------------\nGuess a letter : ")
        print("\n","".join(hintguesses))
        continue

    elif ask_letter in alphabet:

        if ask_letter in shuffled_word:
            hangmanascii()
            print("[✔]'",ask_letter,"'", "is in the word !")
            print("[-] Wrong letters guessed :", wrongguessedword)
            print("\n","".join(hintguesses))
            ask_letter = input("\n-----------------------\nGuess a letter : ")

        else:
            tries += 1
            wrongguessedword.append(ask_letter)
            hangmanascii()
            print("\nWrong letters guessed :", wrongguessedword)
            print("\n[!] Letter not in the word!")
            print("[!] You now have", 8-tries, "attempts remaining")
            print("\n","".join(hintguesses))
            
            if(8-tries == 0):
                lose()

            ask_letter = input("\n-----------------------\nGuess a letter : ")
            if ask_letter in wrongguessedword:
                tries -= 1
                print("[*] You already guessed this letter")   
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