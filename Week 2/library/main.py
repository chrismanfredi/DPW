__author__ = 'Chris'

from library import * # Import the library.py

# Class MainHandler
class MainHandler():
    def __init__(self): # Define Constructor Function
        self.lib = Library()
        self.lib.student = raw_input("What is your name?") # Prompting The User
        self.lib.grade_one = int(raw_input("What is your first grade?")) # Prompting The User
        self.lib.grade_two = int(raw_input("What is your second grade?")) # Prompting The User
        self.lib.grade_three = int(raw_input("What is your third grade?")) # Prompting The User
        self.lib.total = self.lib.mean(self.lib.grade_one,self.lib.grade_two,self.lib.grade_three)

        self.show = Printer()
        self.show.print_out(str(self.lib.student),str(self.lib.total))

app = MainHandler() # Run the main handler class









