# Hangman Game

---

# Project Requirements

- Don't overestimate or underestimate your coding capabilities; work at your skill level.
- The project needs to be completed by October 6th.
- Collaborate with your teams, and ensure that the workload is divided equally.
- Optimize your code at the end to make it more readable and efficient.

---

# Rules

- Maximum of 7 mistakes allowed.
- Only 1 letter can be guessed in each try.
- The word cannot be changed in the middle of the game.
- The game stops when the user finds the word within 7 tries.
- The user can only input letters from 'a' to 'z' (no other data types are allowed; input should only be strings).

---

# Program Requirements

- Text based (No graphics)

---

# Process of the game

1. The program selects a word at random from a given list.
   - 1.1. The program informs the user of the length of the randomly selected word.

2. The user inputs one letter at a time, which can be any letter from 'a' to 'z'.
   - 2.1. The user is allowed to make up to 7 guessing mistakes at most. If the limit of guesses is reached, then the user loses.

3. The program informs the user if the letter corresponds to the word and in what position.
   - 3.1. If the user is wrong, meaning the letter is not in the word, the user needs to try again, and the user also loses a guess.

4. If the user correctly guesses all the letters of the word within the 7 attempts, then the user wins yeay!
