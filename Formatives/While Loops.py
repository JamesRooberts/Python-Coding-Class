
# Age Loop
def ageloop():
    age = int(input("what is your age?"))

    while age < 1:
        print("bro seriously? put a real age in.")
        age = int(input("what is your age?"))
    else:
     print("yay! you are not braindead!")


# Number Game

def numbergame():
    number = int(input("pick a whole number between 1 and 10"))

    while number <=4:
        print("wrong")
        number = int(input("try again:"))
    else: 
        while number >=6:
            print("wrong")
            number = int(input("try again:"))
        else:
            if number == 5:
                print("correct!")
    

