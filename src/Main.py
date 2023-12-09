from Play import Play
from Create import Create
import os

from Fonts import bcolors

def MenuOptions():
    print("1: Play a Mad-Lib!")
    print("2: Create a Mad-Lib!")
    print("3: Exit\n")
    user_input = input()
    return user_input


def start():
    WelcomeMessage()
    GetEnter()
    MainMenu()


def GetEnter():
    user_input = None
    while user_input is None:
        user_input = input()
    os.system('cls')


def MainMenu():
    finish = False
    while not finish:
        option = MenuOptions()
        if option == "1":
            play_game = Play()
            os.system('cls')
            play_game.start()
        elif option == "2":
            create_lib = Create()
            os.system('cls')
            create_lib.start()
        elif option == "3":
            finish = True
        else:
            print(f"{bcolors.FAIL}Invalid option. Please Try Again")
            print(f"{bcolors.WHITE}")

def WelcomeMessage():
    os.system('cls')
    print("--------------------Welcome to Mad-Libs!--------------------\n")
    print("Mad libs are a fun way to pass the time and even better when\n"
          "played with friends! In this game, you can play a mad lib or\n"
          "create a mad lib of your own! You will be presented with the\n"
          "option you want to do in just a minute. Just know, any words\n"
          "you enter will be checked for correctness, so stay in bounds\n"
          "when playing along! Best of luck!\n\n")
    print("                  Press Enter to continue!                  \n")


if __name__ == "__main__":
    start()
