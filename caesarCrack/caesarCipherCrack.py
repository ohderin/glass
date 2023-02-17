cipherText = "w zcjs dobqoysg" # input ciphertext (lowercase letters)

def alphabet():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return(letters)

def dictionary():
    dictionary = open("dictionary.txt")
    wordList = []
    for word in dictionary.read().split('\n'):
        wordList.append(word)
    dictionary.close()
    return(wordList)


def bruteForce(cipherText):
    bestMatch = 0
    bestMatchText = ""
    x = 0
    while x < 26:
        x = x + 1 
        encryptedString = cipherText
        cipherShift = int(x)
        stringDecrypted = ""
        letters = alphabet()
        for character in encryptedString:
            position = letters.find(character)
            newPos = position - cipherShift
            if character in letters:
                stringDecrypted = stringDecrypted + letters[newPos]
            else:
                stringDecrypted = stringDecrypted + character

        wordMatch = 0
    
        for word in stringDecrypted.split(' '):
            word = word.strip(" ")
            word = word.strip(",")
            if word in dictionary():
                wordMatch = wordMatch + 1

        if wordMatch > bestMatch:
            bestMatchText = stringDecrypted

    result = "Most probable plaintext: '" + bestMatchText + "'"
    return(result)

plainText = bruteForce(cipherText)
print(plainText)
