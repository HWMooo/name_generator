import numpy as np
import random

alphabet = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e",
 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l",
13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r",
19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}


def dragon_name(name, dob):
    random_word = ""
    name = name[::-1]
    dob = dob.split("/")
    for numbers in dob:
        numbers = int(numbers)
        if(numbers < 27):
            random_word += alphabet[numbers]
        else:
            random_word += "zq"
    newName = name + random_word
    dragonName = newName

    return dragonName


def penguin_name(name, dob):
    random_word = ""
    name = list(name)
    random.shuffle(name)
    dob = dob.split("/")
    for numbers in dob:
        numbers = int(numbers)
        if(numbers < 27):
            random_word += alphabet[numbers]
        else:
            random_word += "zq"
    penguinName = ''.join(name) + random_word

    return penguinName

def Game():
    exit = False
    name = input("enter your name:")
    dob = input("enter your date of birth as dd/m/yyyy")
    Nametype = input("would you like to be known as your penguin name or dragon name?")
    if Nametype == "dragon name":
        output = f"hello {dragon_name(name, dob)} what would you like to do?"
    else:
        output = f"hello {penguin_name(name, dob)} what would you like to do?"
    while exit == False:
        decision = input(output)
        if(decision == "exit"):
            exit = True
    return 0





Game()