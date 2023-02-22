# Sandwhich Paragraph

("to make a ham sandwhich do the following. first, open the fridge door and grab your bread and ham. then, close the fridge door and walk to the cabinet that contains plates. grab a plate, walk to a counter, and set the plate down. then, take two slices of bread out of the bag of bread, and set bag of bread down on the counter. then take 2 slices of ham and put it on top of the left slice of bread. put the container of ham next to the bag of bread on the counter. take the right slice of bread and flip it over ontop of the left slice of bread. then grab the bread bag, and the container of ham and walk to the fridge. lastly, open the fridge and place both items into the fridge. and youre done! ") 


# Lesser of two Evens

def lesser_of_two_evens(first,second):
        if int(first) > int(second): 
            return second
        else:
            return first
lesserval = lesser_of_two_evens(2, 20)
print(lesserval)

# Animal Crackers

def animal_crackers(words):
    animal, crackers = words.split()
    if animal[0] == crackers[0]:
        return True
    else:
        return False


animalval = animal_crackers("bloop shoop")
print(animalval)

# Makes20

def makes20(first,second):
    if int(first) + int(second) == 20:
        return True
    elif int(first) == 20 or int(second) == 20:
        return True
    else:
        return False

makes20val = makes20(20, 10)
print(makes20val)
