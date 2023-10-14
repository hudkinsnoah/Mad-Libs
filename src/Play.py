import os
import random


class Play:
    def __init__(self):
        self.MasterListName = os.path.abspath(os.path.join(os.getcwd(), "..", "MadLibs", "MasterList.txt"))
        self.MasterList = None
        self.MadLib = ""
        self.PromptsList = []
        self.MadLibName = None

    def start(self):
        self.GetMadLib()
        self.ParseMadLib()
        self.PromptInput()
        self.ParseTogether()
        self.PrintMadLib()

    def GetMadLib(self):
        self.OpenMasterList()
        MadlibIndex = random.randint(0, len(self.MasterList) - 1)
        self.MadLibName = self.MasterList[MadlibIndex].strip()
        self.GetChosenMadLib(self.MadLibName)

    def OpenMasterList(self):
        try:
            file = open(self.MasterListName, 'r')
            self.MasterList = file.readlines()
        except OSError as error:
            print(error)
            exit(1)

    def GetChosenMadLib(self, MadLibName):
        file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "MadLibs", f"{MadLibName}.txt")), "r")
        self.MadLib = file.readlines()
        self.MadLib = self.MadLib[0]

    def ParseMadLib(self):
        star_list = []
        for index in range(0, len(self.MadLib)):
            if self.MadLib[index] == "*":
                star_list.append(index)

        if len(star_list) % 2 != 0:
            print(f"Uneven number of *. Please check the MadLib named {self.MadLibName}")

        for prompt in range(0, len(star_list), 2):
            self.PromptsList.append([star_list[prompt], star_list[prompt + 1],
                                     self.MadLib[star_list[prompt]:star_list[prompt +1] + 1]])

    def PromptInput(self):
        for prompt in range(0, len(self.PromptsList)):
            print(f"Enter a(n): {self.MadLib[self.PromptsList[prompt][0] + 1:self.PromptsList[prompt][1]]}")
            user_input = input()
            self.PromptsList[prompt].append(user_input)

    def ParseTogether(self):
        for prompt in self.PromptsList:
            self.MadLib = self.MadLib.replace(prompt[2], prompt[3], 1)

    def PrintMadLib(self):
        print("Here is the Final Result!")
        count = 0
        madLibRemaining = len(self.MadLib)
        while count < len(self.MadLib):
            if madLibRemaining < 60:
                print(self.MadLib[count:])
                count += madLibRemaining
                madLibRemaining = 0
            else:
                print(self.MadLib[count:count + 60])
                count += 60
                madLibRemaining -= 60
