import pygame
import random

words = []  # empty Array to Store words
file = open("google-10000-english-no-swears.txt", "rt")
for w in file:
    word = str(w)
    word = word.rstrip("\n")
    if len(word) > 3:
        words.append(word)
file.close()

gameState = True
Lives = 6
lettersused = []


def containsletter(character):
    global lettersused
    global Lives

    if not character in lettersused:
        if character in hiddenWord:
            for i in range(0, len(hiddenWord)):  # in range because need to find the indice!
                if hiddenWord[i] == character:
                    hiddenWordArray[i] = character
            lettersused.append(character)
        else:
            Lives -= 1
            lettersused.append(character)


def containsword(word):
    if hiddenWord == word:
        print("You found the Word!")
    else:
        print("\nYou didn't find the Word... :(\nThe word was: " + hiddenWord)


if __name__ == '__main__':
    hiddenWord = random.choice(words)  # randomly choosing a word
    hiddenWordArray = []
    for char in hiddenWord:
        hiddenWordArray.append("_")
    hiddenWordFind = "".join(str(x) for x in hiddenWordArray)
    print(hiddenWordFind)

    while gameState:
        print("Pick a Letter or Word")
        while True:  # verify if the input is only Letters or Words
            userInput = input("Letter/Word: ").lower()
            if not userInput.isalpha():
                print("Only letters or words are accepted!")
                continue  # if it isn't it continues the loop until it's a Letter or Word
            else:
                break  # once it's a letter or word, exits the loop
        if len(userInput) < 2:  # checks to see if the input is a Letter or a Word
            containsletter(userInput)
            hiddenWordFind = "".join(str(x) for x in hiddenWordArray)
            print(hiddenWordFind)
            if Lives < 0:
                print("\nYou didn't find the Word... :(\nThe word was: " + hiddenWord)
                gameState = False

        else:
            containsword(userInput)
            gameState = False
        if hiddenWordFind == hiddenWord:
            print("\nYou found the Word!!\n Congratulations!")
            print(hiddenWordFind)
            gameState = False
