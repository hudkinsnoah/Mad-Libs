import os
import random
from Fonts import bcolors


WORD_FILES = {"verbs": "verbs.txt", "adjectives": "adjectives.txt",
              "nouns": "nouns.txt", "bodyparts": "bodyparts.txt",
              "animals": "animals.txt", "clothes": "clothes.txt",
              "rooms": "rooms.txt"}

class Play:
    def __init__(self):
        self.MasterListName = os.path.abspath(os.path.join(os.getcwd(), "..", "MadLibs", "MasterList.txt"))
        self.MasterList = None
        self.MadLib = ""
        self.PromptsList = []
        self.MadLibName = None
        self.verbs = dict()
        self.adjectives = dict()
        self.nouns = dict()
        self.bodyparts = dict()
        self.animals = dict()
        self.clothes = dict()
        self.rooms = dict()

    def start(self):
        self.ReadWords()
        self.GetMadLib()
        self.ParseMadLib()
        self.PromptInput()
        self.ParseTogether()
        self.PrintMadLib()

    def start_specific(self, name):
        os.system('cls')
        self.ReadWords()
        self.GetSpecificMadLib(name)
        self.ParseMadLib()
        self.PromptInput()
        self.ParseTogether()
        self.PrintMadLib()

    def GetMadLib(self):
        self.OpenMasterList()
        MadlibIndex = random.randint(0, len(self.MasterList) - 1)
        self.MadLibName = self.MasterList[MadlibIndex].strip()
        self.GetChosenMadLib(self.MadLibName)

    def GetSpecificMadLib(self, name):
        try:
            file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "MadLibs", f"{name}.txt")), 'r')
            self.MadLib = file.readlines()
            self.MadLib = self.MadLib[0]
            file.close()
        except OSError as error:
            print(error)
            exit(1)

    def OpenMasterList(self):
        try:
            file = open(self.MasterListName, 'r')
            self.MasterList = file.readlines()
            file.close()
        except OSError as error:
            print(error)
            exit(1)

    def GetChosenMadLib(self, MadLibName):
        file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "MadLibs", f"{MadLibName}.txt")), "r")
        self.MadLib = file.readlines()
        self.MadLib = self.MadLib[0]
        file.close()

    def ParseMadLib(self):
        star_list = []
        for index in range(0, len(self.MadLib)):
            if self.MadLib[index] == "*":
                star_list.append(index)

        if len(star_list) % 2 != 0:
            print(f"{bcolors.FAIL}Uneven number of *. Please check the MadLib named {self.MadLibName}")
            print(f"{bcolors.WHITE}")

        for prompt in range(0, len(star_list), 2):
            self.PromptsList.append([star_list[prompt], star_list[prompt + 1],
                                     self.MadLib[star_list[prompt]:star_list[prompt +1] + 1]])

    def PromptInput(self):
        for prompt in range(0, len(self.PromptsList)):
            print(f"Enter a(n): {self.MadLib[self.PromptsList[prompt][0] + 1:self.PromptsList[prompt][1]]}")
            user_input = self.CheckForInput(self.MadLib[self.PromptsList[prompt][0] + 1:self.PromptsList[prompt][1]])
            self.PromptsList[prompt].append(user_input)

    def CheckForInput(self, given_type):
        valid_input = False
        while not valid_input:
            user_input = input()
            if given_type == "adjective":
                if user_input.strip().lower() not in self.adjectives:
                    print(f"{bcolors.WARNING}Does not appear to be a valid adjective. Please try again")
                    print(f"{bcolors.WHITE}")
                    continue
            elif given_type == "animal" or given_type == "type of bug":
                if user_input.strip().lower() not in self.animals:
                    print(f"{bcolors.WARNING}Does not appear to be a valid animal. Please try again")
                    print(f"{bcolors.WHITE}")
                    continue
            elif "part of the body" in given_type or given_type == "body part" and "plural" not in given_type:
                if user_input.strip().lower() not in self.bodyparts:
                    print(f"{bcolors.WARNING}Does not appear to be a valid part of the body. Please try again")
                    print(f"{bcolors.WHITE}")
                    continue
            elif given_type == "clothing item":
                if user_input.strip().lower() not in self.clothes:
                    print(f"{bcolors.WARNING}Does not appear to be a valid clothing item. Please try again")
                    print(f"{bcolors.WHITE}")
                    continue
            elif given_type == "noun":
                if user_input.strip().lower() not in self.nouns:
                    print(f"{bcolors.WARNING}Does not appear to be a valid noun. Please try again")
                    print(f"{bcolors.WHITE}")
                    continue
            elif given_type == "verb":
                if user_input.strip().lower() not in self.verbs:
                    print(f"{bcolors.WARNING}Does not appear to be a valid verb. Please try again")
                    print(f"{bcolors.WHITE}")
                    continue
            elif "ending in \"ing\"" in given_type:
                if not user_input.lower().endswith("ing"):
                    print(f"{bcolors.WARNING}Does not end with 'ing'. Please try again")
                    print(f"{bcolors.WHITE}")
                    continue
            elif given_type == "number":
                if not user_input.isnumeric():
                    print(f"{bcolors.WARNING}Does not appear to be a valid number. Please try again")
                    print(f"{bcolors.WHITE}")
                    continue
            elif given_type == "room in a house" or given_type == "room of the house":
                if user_input.lower() not in self.rooms:
                    print(f"{bcolors.WARNING}Does not appear to be a valid room. Please try again")
                    print(f"{bcolors.WHITE}")
                    continue
            valid_input = True

        return user_input

    def ParseTogether(self):
        for prompt in self.PromptsList:
            self.MadLib = self.MadLib.replace(prompt[2], prompt[3], 1)

    def PrintMadLib(self):
        os.system('cls')
        print("Here is the Final Result!")
        count = 0
        madLibRemaining = len(self.MadLib)
        while count < len(self.MadLib):
            if madLibRemaining < 80:
                print(self.MadLib[count:])
                count += madLibRemaining
                madLibRemaining = 0
            else:
                print(self.MadLib[count:count + 80])
                count += 80
                madLibRemaining -= 80
        # Get a blank line in the output this way
        print()

    def ReadWords(self):
        animals_file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "words", f"{WORD_FILES['animals']}")), 'r')
        Lines = animals_file.readlines()
        for line in Lines:
            self.animals[line.strip().lower()] = line.strip().lower()
        animals_file.close()

        adjectives_file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "words", f"{WORD_FILES['adjectives']}")),
                               'r')
        Lines = adjectives_file.readlines()
        for line in Lines:
            self.adjectives[line.strip().lower()] = line.strip().lower()
        adjectives_file.close()

        bodyparts_file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "words", f"{WORD_FILES['bodyparts']}")),
                               'r')
        Lines = bodyparts_file.readlines()
        for line in Lines:
            self.bodyparts[line.strip().lower()] = line.strip().lower()
        bodyparts_file.close()

        clothes_file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "words", f"{WORD_FILES['clothes']}")),
                               'r')
        Lines = clothes_file.readlines()
        for line in Lines:
            self.clothes[line.strip().lower()] = line.strip().lower()
        clothes_file.close()

        nouns_file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "words", f"{WORD_FILES['nouns']}")),
                               'r')
        Lines = nouns_file.readlines()
        for line in Lines:
            self.nouns[line.strip().lower()] = line.strip().lower()
        nouns_file.close()

        verbs_file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "words", f"{WORD_FILES['verbs']}")),
                               'r')
        Lines = verbs_file.readlines()
        for line in Lines:
            self.verbs[line.strip().lower()] = line.strip().lower()
        verbs_file.close()

        rooms_file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "words", f"{WORD_FILES['rooms']}")), 'r')
        Lines = rooms_file.readlines()
        for line in Lines:
            self.rooms[line.strip().lower()] = line.strip().lower()
        rooms_file.close()
