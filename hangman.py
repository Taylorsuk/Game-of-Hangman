import random
import re
# start with a list of words for the player to guess
wordsToGuess = ['javascript', 'python', 'algorithm', 'vscode', 'cobol', 'complier', 'angular', 'react', 'svelt']
allowedGuesses = 10
incorrectGuesses = []
correctGuesses = []
randomWord = random.choice(wordsToGuess)
guessWord = []

# we have a random word so we can now start the game
print("Lets play a game of Dev Hangman")

for character in randomWord:
    guessWord.append('_')

# while they still have guesses in the bank run this loop
while allowedGuesses - len(incorrectGuesses) > 0:

    # get an input from the user
    letterGuess = input('\n\nGuess a letter: ').lower()

    # check that its a valid letter (and they actually entered something!)
    if not re.match("^[a-z]*$", letterGuess):
        print('You can only enter a character from the alphabet (a - z)')
        continue
    elif len(letterGuess) > 1 or len(letterGuess) == 0:
        print("You must enter a single character")
        print(letterGuess)
        continue
    # already tried the letter
    elif (letterGuess in correctGuesses) or (letterGuess in incorrectGuesses):
        print("You have already tried {}, try another letter".format(letterGuess))
        continue

    # letter is in the word
    letterIndex = randomWord.find(letterGuess)
    if letterIndex >= 0:  # letterGuess in randomWord:
        correctGuesses.append(letterGuess)
        print('awesome guess, {} is in the word'.format(letterGuess))
        guessWord[letterIndex] = letterGuess

    # incorrect guess
    else:
        # push the incorrect guess to the incorrect guess list and
        incorrectGuesses.append(letterGuess)
        # calculate the guesses remaining
        remaining = allowedGuesses - len(incorrectGuesses)
        # notify the user
        print("Sorry, you lose a life, {} is not in the secret word, {} guesses remaining".format(letterGuess, remaining))

        # check if that was their last life
        if remaining == 0:
            print('sorry, you failed to guess the word: {}, why not give it another go!'.format(randomWord))
            break

        print('Incorrect guesses: {}'.format(incorrectGuesses))

    # show current status
    print('Your progress: {}'.format(''.join(guessWord)))

    # they have guessed all the letters Winner!
    if len(correctGuesses) == len(randomWord):
        print('You won the game!')
        break
