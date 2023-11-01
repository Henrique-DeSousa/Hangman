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
letters_used = []


def contains_letter(character):
    global letters_used
    global Lives

    if character not in letters_used:
        if character in hiddenWord:
            for i in range(0, len(hiddenWord)):  # in range because need to find the indices!
                if hiddenWord[i] == character:
                    hiddenWordArray[i] = character
            letters_used.append(character)
        else:
            Lives -= 1
            letters_used.append(character)


def contains_word(word_input):
    if hiddenWord == word_input:
        print("\nYou found the Word!!\nCongratulations!")
    else:
        print("\nYou didn't find the Word... :(\nThe word was: " + hiddenWord)


def check_alpha():
    while True:  # verify if the input is only Letters or Words
        user_input = input("").lower()  # makes it so the userInput is always lowerCase
        if not user_input.isalpha():
            print("Only letters or words are accepted!")
            continue  # if it isn't it continues the loop until it's a Letter or Word
        else:
            return user_input  # once it's a letter or word, exits the loop


if __name__ == '__main__':
    while gameState:
        Lives = 6
        hiddenWord = random.choice(words)  # randomly choosing a word
        hiddenWordArray = []
        letters_used = []
        for char in hiddenWord:
            hiddenWordArray.append("_")
        hiddenWordFind = "".join(str(x) for x in hiddenWordArray)
        print(hiddenWordFind)
        while not Lives < 0:
            print(letters_used)
            print(Lives)
            print("Pick a Letter or Word\nLetter/Word: ")
            user_input = check_alpha()
            if len(user_input) < 2:  # checks to see if the input is a Letter or a Word
                contains_letter(user_input)
                hiddenWordFind = "".join(str(x) for x in hiddenWordArray)
                print(hiddenWordFind)
                if Lives < 0:
                    print("\nYou didn't find the Word... :(\nThe word was: " + hiddenWord)
                    gameState = False
            else:
                contains_word(user_input)
                gameState = False
                Lives = -1
            if hiddenWordFind == hiddenWord:
                print("\nYou found the Word!!\nCongratulations!")
                print(hiddenWordFind)
                gameState = False
                Lives = -1
        if not gameState:
            print("\nPlay again? (y/n)")
            user_input = check_alpha()
            if user_input == "yes" or user_input == "y":
                gameState = True
            else:
                exit(0)
