# Incomplete
import os
import random

def game():
    with open("./files/data.txt","r",encoding="UTf-8") as data:
            words = [word for word in data]
            print(words)
            word = random.choice(words)
            random_word = word(words)
            print(random_word)


    with open("./files/game.txt","w",encoding="UTF-8") as file:
        print(words)
        letter = input("Put a letter: ")

def main():
    os.system("cls")
    #Print the game
    game()

if __name__ == "__main__":
    main()