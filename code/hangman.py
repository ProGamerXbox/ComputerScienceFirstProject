import random

hangman_list = open('wordlist.txt').read().splitlines()
alphabet = open('alphabet.txt').read().splitlines()


def replay_game():
    global tries
    response = input("Would you like to play again? (y/n): ")
    if response.lower() == 'y':
        tries = 1
        play_game()
    elif response.lower() == 'n':
        exit()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        replay_game()

def hangmanascii():
    HANGMANPICS = ['',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']
    print(HANGMANPICS[tries])

def lose():
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
    print('\nThe word was', "'", shuffled_word, "'\n")
    replay_game()
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
    replay_game()

def start():
    global tries,hangman_list,shuffled_word,shuffled_word,word_length,alphabet,wrong_guessed_word,hintguesses,ask_letter
    
    shuffled_word = random.choice(hangman_list)
    word_length = len(shuffled_word)
    tries = 1
    wrong_guessed_word = []

    hintguesses = ['_'] * len(shuffled_word)
    print("".join(hintguesses))

    print("""
     _    _          _   _  _____ __  __          _   _ 
    | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
    | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
    |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
    | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
    |_|__|_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
    / ____|    /\   |  \/  |  ____|                   
    | |  __   /  \  | \  / | |__    Made by :                    
    | | |_ | / /\ \ | |\/| |  __|        - Tom           
    | |__| |/ ____ \| |  | | |____       - William          
    \ _____/_/    \_\_|  |_|______|      - Marius    
    """)

    print("\nThe word you are looking for is", word_length, "characters long")

    ask_letter = input("\n-----------------------\nGuess a letter : ")

def play_game():
    global tries,hangman_list,shuffled_word,shuffled_word,word_length,alphabet,wrong_guessed_word,hintguesses,ask_letter
    start()
    while tries <= 7:
        if '_' not in hintguesses:
            win()

        if len(ask_letter) != 1 or ask_letter.lower() not in alphabet:
            print("/!\ Your guess must be a single letter from the alphabet /!\ ")
        elif ask_letter in wrong_guessed_word:
            print("[*] You already guessed this letter")
        elif ask_letter in shuffled_word:
            hangmanascii()
            print("[✔]'", ask_letter, "'", "is in the word!")
            print("[-] Wrong letters guessed:", wrong_guessed_word)
            for index, letter in enumerate(shuffled_word):
                if letter == ask_letter:
                    hintguesses[index] = ask_letter
            print("\n", "".join(hintguesses))
        else:
            tries += 1
            wrong_guessed_word.append(ask_letter)
            hangmanascii()
            print("\nWrong letters guessed:", wrong_guessed_word)
            print("\n[!] Letter not in the word!")
            print("[!] You now have", 8 - tries, "attempts remaining")
            print("\n", "".join(hintguesses))
            if tries == 8:
                lose()
        ask_letter = input("\n-----------------------\nGuess a letter : ")

play_game()