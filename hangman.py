import random

# start with a list of words for the player to guess
wordsToGuess = ['javascript', 'python', 'algorythm', 'vscode', 'cobol', 'complier', 'angular', 'react', 'svelt']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
allowedGuesses = 10
incorrectGuesses = []
correctGuesses = []
randomWord = random.choice(wordsToGuess)
wordLength = len(randomWord)
# we have a random word so we can now start the game

print("Lets play a game of Dev Hangman")
print(wordLength)

# while they still have guesses in the bank run this loop
while allowedGuesses - len(incorrectGuesses) > 0:

    # get an input from the user
    letterGuess = input('Guess a letter: ')
    print(letterGuess)


    # letter is in the word
    if letterGuess in wordsToGuess:
        print(letterGuess)

    # already tried the letter
    # notify the user
    elif (letterGuess in correctGuesses) or (letterGuess in incorrectGuesses):
        print('Already tried {letterGuess}')

    # incorrect guess
    else:
        print("else")
    # notify the user
    # remove a life if they have any left


# they have guessed all the letters Winner!


# If they have run out of lives then it's game over :(
if allowedGuesses - len(incorrectGuesses) == 0:
    print("Game over unfortunately")


else:
    print("here")
