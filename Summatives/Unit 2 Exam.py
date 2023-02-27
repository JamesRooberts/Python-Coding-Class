# Code Example: if statement

# Getting name

name = str(input("What is your name?"))

# if, elif, and else statements

if len(name) <= 3:
    print("woah buddy, you have a short name")
elif len(name) <= 7:
        print("okay, you have a decent sized name")
elif len(name) <= 12:
        print("okay, you have a pretty big name")
else:
    print("okay dude, thats a HUGE name")

# Code Example: for loop

lst = ["apple", "banana", "orange"]
     
     
     




# Code Example: while loop

#grabbing the answer

answer = int(input("What is 2 + 2"))

# is it right?

while answer != 4:
    print("nope you are dumb")
    answer = int(input("What is 2 + 2"))
else:
    print("yay you are not braindead")

# Code Example: function

def Function():
    name = str(input("What is your name?"))
    while name.isnumeric:
         name = str(input("What is your name?"))
    else:
         return 'nice!'






Function()