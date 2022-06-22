#Thomas Evans
#CS1181 evening
#Cipher

import random

alph = "abcdefghijklmnopqrstuvwxyz " #index for math


def check_key(): #Check that key is valid and randomizer
    global input_key
    if input_key < 0 or input_key > 25 and input_key != 100:
        input_key = int(input("Choose and input key. 0-25 or 100 for a random key."))
        check_key()
    elif input_key == 100:
        input_key = random.randrange(26)

def encrypt(): #does the acctual encryption
    word_lower = plaintext.lower()
    encoded = ""
    for char in word_lower:
        code = 0
        code += alph.find(char)
        code_plus_key = code + input_key
        if code != 26:
            if code_plus_key > 25:
                code_plus_key -= 26
            encoded += alph[code_plus_key]
        else:
            encoded += " "
    print(encoded)

def word_check(): #checks that the string only has letters and or spaces
    global plaintext
    global testneeded
    testneeded = True
    if len(plaintext) > 250:
        plaintext = input("Type the plaintext you want to encrypt.")
    while testneeded == True: #keeps going until the testneeded check is flipped
        word_lower = plaintext.lower()
        for char in word_lower:
            check = 0
            check += alph.find(char)
            if check < 0:
                plaintext = input("Type the plaintext you want to encrypt.")
                break
            else:
                testneeded = False #stops loop if no invalid character is found

def run():
    global input_key
    global plaintext
    input_key = int(input("Choose and input key. 0-25 or 100 for a random key."))
    check_key()
    plaintext = input("Type the plaintext you want to encrypt.")
    word_check()
    encrypt()
    again = input("Again? (y/n)")
    yes = bool
    while yes != True or yes != False:
        if again.lower() == "y":
            yes = True
            run()
        elif again.lower() == "n":
            yes = False
            break
run()
