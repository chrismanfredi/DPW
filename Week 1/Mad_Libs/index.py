__author__ = 'Chris'

# Strings
name = raw_input("What is your name?")
born = raw_input("What year were you born in?")
school = raw_input("What is the name of your school?")
hometown = raw_input("What school is your town in?")
car = raw_input("What kind of car do you drive?")

# for loop

welcome = ["Welcome To Mad Libs!, ", name]

for w in welcome:
    print w

#function

def print_out(n,b,s,h,c):
    print("hello my name is " + n + ". I attend " + s + ", which is in the town of "
+ h + ". I was born in the year " + b + ", I drive a " + c + ".")

# Getting the length of your name

def add(n):
    total = len(n)
    return total

# If Statement

if name > 5:
    print ("cool name")
else:
    print("your name sucks!")


# Printing the string name
print "your name is " + str(add(name)) + " Characters long!"

print_out(name,born,school,hometown,car)



