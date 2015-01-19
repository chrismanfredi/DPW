__author__ = 'Chris'

class Library: # Library Class
    def __init__(self): #define the function
        self.student = ""
        self.grade_one = 0
        self.grade_two = 0
        self.grade_three = 0
        self.total = 0

    def mean(self,x,y,z): # Define the mean function
        total = x + y + z
        return total /3 # divide the total by 3


class Printer(): # Printer Class
    def print_out(self,name,avg):
        print "Hello "+ name + " your average is " + str(avg) # Printing the name and average






