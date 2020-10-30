import random
import re

# import the wordlist
txtfile = open('word_list.txt', 'r')
wordsToGuess = txtfile.readlines()
allowedGuesses = 7
incorrectGuesses = []
correctGuesses = []
randomWord = random.choice(wordsToGuess).strip()
guessWord = []
maskCharacter = '*'

# we have a random word so we can now start the game
print("Lets play a game of Hangman")

for character in randomWord:
    guessWord.append(maskCharacter)

print("The word you are trying to guess is {}".format(''.join(guessWord)))


def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


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
        print("You have already tried {}. Please enter your next guess: {}".format(letterGuess, ''.join(guessWord)))
        continue

    # letter is in the word
    # letterIndex = randomWord.find(letterGuess)
    letterIndices = findOccurrences(randomWord, letterGuess)
    # if letterIndex >= 0:
    if len(letterIndices) > 0:
        correctGuesses.append(letterGuess)
        print('awesome guess, "{}" is in the word.'.format(letterGuess))

        for letterIndex in letterIndices:
            guessWord[letterIndex] = letterGuess

    # incorrect guess
    else:
        # push the incorrect guess to the incorrect guess list and
        incorrectGuesses.append(letterGuess)
        # calculate the guesses remaining
        remaining = allowedGuesses - len(incorrectGuesses)
        # notify the user
        print("Sorry, you lose a life, '{}' is not in the secret word, {} guesses remaining. \n\n Please enter your next guess: {}".format(
            letterGuess, remaining, ''.join(guessWord)))

        # check if that was their last life
        if remaining == 0:
            print('Sorry, you failed to guess the word: "{}", you lose, why not give it another go!'.format(randomWord))
            break

        print('Incorrect guesses: "{}"'.format(incorrectGuesses))

    # show current status
    print('Please enter your next guess: {}'.format(''.join(guessWord)))

    # let's see how many remaining stars there are:
    remainingStars = findOccurrences(guessWord, maskCharacter)

    # they have guessed all the letters Winner!
    # if len(correctGuesses) == len(randomWord):
    if len(remainingStars) == 0:
        print('Congratulations you win')
        break
