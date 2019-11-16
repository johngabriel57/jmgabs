def getGuessedWord(secretWord, lettersGuessed):
    
    guess= ''
    for char in secretWord:
        if char in lettersGuessed:
            guess= guess + char
        else:
            guess= guess + ' _ '
    return guess
