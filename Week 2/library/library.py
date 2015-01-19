__author__ = 'Chris'

class Library: # Library Class
    def __init__(self): # define the function
        self.student = "" # Student Name
        self.grade_one = 0 # Student Grade 1
        self.grade_two = 0 # Student Grade 2
        self.grade_three = 0 # Student Grade 3
        self.total = 0 # Total of grades

    def mean(self,x,y,z): # Define the mean function
        total = x + y + z # Adding Grades
        return total /3 # divide the total by 3


class Printer(): # Printer Class
    def print_out(self,name,avg): # Print Out Function
        print "Hello "+ name + " your average is " + str(avg) # Printing the name and average






