from pynput import keyboard
import os

class Create:
    def __init__(self):
        self.MasterListName = os.path.abspath(os.path.join(os.getcwd(), "..", "MadLibs", "MasterList.txt"))
        self.temp = 1
        self.title = ""
        self.mad_lib = ""
        self.done_input = False
        self.done_confirmed = False

    def start(self):
        print("Here, you can  create your  own  Mad Lib!")
        print("Create  your  story  while  prompting for")
        print("some input  from  a player. To  prompt  a")
        print("User for input, place your prompt between")
        print("two asterisks(*). For example: *verb* and")
        print("continue one with your story!  To finish,")
        print("press the Escape key,  then the Enter key")
        print("             Happy Libbing!              ")
        self.get_title()
        self.start_keyboard_listener()
        self.get_mad_lib_input()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.done_input = True

    def get_title(self):
        print("\nPlease enter the title of your Mad Lib!")
        self.title = input()

    def get_mad_lib_input(self):
        print("Please enter the Mad Lib!")
        while not self.done_confirmed:
            while not self.done_input:
                new_input = input()
                self.mad_lib += new_input

            done = self.confirm_done()
            if not done:
                self.done_input = False
            else:
                self.done_confirmed = True
        check_successful = self.check_input()
        if check_successful:
            self.save_madlib()

    def check_input(self):
        asterisk_count = 0
        for character in self.mad_lib:
            if character == '*':
                asterisk_count += 1

        if asterisk_count % 2 != 0:
            print("Error: There was an uneven number of asterisks given in the input")
            return False

        return True

    def save_madlib(self):
        self.title = self.title.replace(' ', '')
        try:
            new_madlib_file = open(os.path.abspath(os.path.join(os.getcwd(), "..", "MadLibs", f"{self.title}.txt")), 'x')
            new_madlib_file.write(self.mad_lib)
            new_madlib_file.close()
        except IOError:
            print("Error: Madlib name is already taken. Please enter a new Title")
            return
            #TODO: Add ability to enter a new title

        file = open(self.MasterListName, 'a')
        file.write(f"\n{self.title}")
        file.close()

    @staticmethod
    def confirm_done():
        print("Are you sure that you are done inputting your mad lib? (Y/N)")
        done = input().lower()
        if done in ["y", "yes", "yep"]:
            return True
        return False

    def start_keyboard_listener(self):
        self.listener = keyboard.Listener(
            on_release=self.on_release)
        self.listener.start()