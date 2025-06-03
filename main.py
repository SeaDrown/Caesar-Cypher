# Made by Marvin Omoruyi, distributed under the MIT licence.

# This is a Caesar cypher project, which takes in a string, and moves in steps to decrypt it. Only roman alphabetic characters will
# be decrypted. Any other characters in the input string will remain the same.

# You can replace the alphabet with any other string, for example, to Cyrllic or to Greek. Just replace the alphabet variable

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetLength = len(alphabet)
alphabetDict = dict()

def Step(letter:str, step:int):
    """ Takes in a letter and the step amount, and return the decryption."""

    newIndex = alphabetDict[letter] + step

    if newIndex >= alphabetLength:
        newIndex -= alphabetLength
    elif newIndex < 0:
        newIndex += alphabetLength
    
    return alphabet[newIndex]
    

def main():
    for index, char in enumerate(alphabet):
        alphabetDict[char] = index
    
    message = input("What message would you like to decrypt? ")
    step = int(input("What is the step you would like to test? ")) % alphabetLength

    trueMessage = ""

    print(step)

    for i in message:
        i = i.upper()

        if i in alphabetDict:
            trueMessage += Step(i, step)
        else:
            trueMessage += i

    print("This is the decrypted message:", trueMessage)

main()