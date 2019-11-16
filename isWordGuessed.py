def isWordGuessed(secretWord, lettersGuessed):
    
    num= 0
    for char in secretWord:
        if char in lettersGuessed:
            num += 1
        else: 
            return False
        
    return True
