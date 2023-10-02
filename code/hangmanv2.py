import random
guesses = 7
tries = 1
words = ["apple", "orange", "computer", "book", "pen"]
index = random.randint(0, len(words) - 1)
word = words[index]
word_length = len(word)

print(index)

print("\n\nThe word you are looking for is",word_length, "characters long\n")

guess = input("Enter a letter : ")

while tries != 7:

    if (len(guess)) != 1:
        print("Only one letter please, dont cheat")
        guess = input("Enter a letter : ")
    if guess in word[index]:
        print("ITS IN THE WORD!!!")
        guess = input("Enter a letter : ")
    else:
        print("That isn't in the word! You lost a guess!")
        print("you now have", guesses - 1, " attempts remaining")
        guesses -= 1
        tries += 1
        guess = input("Enter a letter : ")



 

if tries == 7:
    print ("The word was " + str(word))