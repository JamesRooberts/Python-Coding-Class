


# Yoinking Math

firstnumber = float(input("what is your first number?: "))
secondnumber = float(input("what is your second number?: "))
operator = input("what is your operator? (+, -, /, *) ")

# other stuff

if operator == "+":
        answerplus = firstnumber + secondnumber
        print(f"Your answer is: {answerplus}")
elif operator == "-":
        answerminus = firstnumber - secondnumber
        print(f"Your answer is: {answerminus}")
elif operator == "/":
        answerdivision = firstnumber / secondnumber
        print(f"Your answer is: {answerdivision}")
elif operator == "*":
        answermultiply = firstnumber * secondnumber
        print(f"Your answer is: {answermultiply}")
else:
    print("good try buddy. do the whole thing again")

    