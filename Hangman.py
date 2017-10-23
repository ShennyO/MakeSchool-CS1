import random

def loadWord():
   f = open('hangman_words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = random.choice(wordsList)
   return secretWord
pass




def isWordGuessed(secretWord, lettersGuessed):

    # FILL IN YOUR CODE HERE...
    'Count becomes 0 everytime you call WordGuessed, turns the word into a list and loop through it.'
    'If that letter is in our userGuessed Array, increase count by 1, if count is equal to length of word, you win the game'
    count = 0
    secretwordlist = list(secretWord)
    for index in range(len(secretwordlist)):
        'if lettersGuessed.contains(secretWord[index]):'
        if secretwordlist[index] in lettersGuessed:
            count += 1
    if count == len(secretWord):
        print("Congratulations! You guessed the word!")
        quit()
    else:
        return False
pass






def getGuessedWord(secretWord, lettersGuessed):

    # FILL IN YOUR CODE HERE...

    secretwordlist = list(secretWord)

    word = []
    for x in range(len(secretWord)):
        word.append("_")
    'Loop through secretWord, and if letters guessed contains that letter, get that index and replace it in our word array.'
    for x in range(len(secretwordlist)):

        if secretwordlist[x] in lettersGuessed:
            word = word[:x] + list(secretWord[x]) + word[x + 1:]

    return word

pass



def user_input(lettersGuessed, secretWord):
    'Get the letter from User, check if it has already been used'
    'add it to userGuessed array, check if letter is in secretwordlist'
    ' if it is not, decrease global count'
    letter = (input("Guess a letter: "))
    global loop_count
    secretwordlist = list(secretWord)
    if letter in lettersGuessed:
        print("You already guessed that letter. Try again!")
        user_input(lettersGuessed, secretWord)
    else:
        lettersGuessed.append(letter)
        if letter in secretwordlist:
            print("Woohoo you got one!")
        else:
            loop_count -= 1

pass



loop_count = 6

def hangman():


    global loop_count
    secret_word = loadWord()
    user_words = []



    while loop_count > 0:

        isWordGuessed(secret_word, user_words)

        word = getGuessedWord(secret_word, user_words)
        print("You have %s left!" % loop_count)
        print("So far you have guessed these letters: %s" %(user_words))
        print(word)
        user_input(user_words, secret_word)
        if loop_count == 0:
            print("Game Over, you lose")
            print(secret_word)
            quit()


pass


hangman()
