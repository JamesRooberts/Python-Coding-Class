# Code Example: if statement

# Getting name

name = str(input("What is your name?"))

# if, elif, and else statements

# if name is short, print this

if len(name) <= 3:
    print("woah buddy, you have a short name")

# if name is decently long, print this


elif len(name) <= 7:
        print("okay, you have a decent sized name")

# if name is long, print this


elif len(name) <= 12:
        print("okay, you have a pretty big name")

# if name is SUPER LONG, print this
    
else:
    print("okay dude, thats a HUGE name")

# Code Example: for loop

odds = 0
    
for x in range(10):
   
# cheking if odd

   if (x % 2) == 1:
       odds += 1
      
# printing every odd

       print(x)
       print(f"{odds} Dang!")

# Code Example: while loop

#grabbing the answer

answer = int(input("What is 2 + 2"))

# is it right?

while answer != 4:
    print("nope you are dumb")
    answer = int(input("What is 2 + 2"))
    if answer == 4:
         break


# Code Example: function

def Function():
    name = input("What is your name?")
    while name.isnumeric():
        print("Nope, that's a number.")
        name = input("What is your name?")

# if name is a string, print you are cool!

    else:
        while name == str:
             print("Cool, your name is", name)
             break


         





Function()