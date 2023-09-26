# Hangman Game

---

# Rules

- 7 maximum mistakes allowed
- only 1 letter can be guessed each try
- the word cannot be changed in the middle of the game
- the game stops when the user found the word within 7 tries
- the user can only inputs letters from a-z (no other datatypes allowed, should only be strings)

---

# Process of the game

1. The program selects a word at random from a given list.
   - 1.1. The program informs the user of the length of the randomly selected word.

2. The user inputs one letter at a time, which can be any letter from 'a' to 'z'.
   - 2.1. The user is allowed to make up to 7 guessing mistakes at most. If the limit of guesses is reached, then the user loses.

3. The program informs the user if the letter corresponds to the word and in what position.
   - 3.1. If the user is wrong, meaning the letter is not in the word, the user needs to try again, and the user also loses a guess.

4. If the user correctly guesses all the letters of the word within the 7 attempts, then the user wins yeay!


---

# Program Requirements

- Text based (No graphics)

---

# Project Requirements

- don't over or under estimate your coding capabilities (code something at your level)
- project needs to be handed on the 6th october
- work with your teams, work should be split up equally
- optimise your code at the end, making it more readable and efficient
