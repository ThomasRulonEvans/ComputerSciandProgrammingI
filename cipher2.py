import random

def cipher(word,keyin):
    new_word = ""
    for char in word.lower():
        if ord(char) != 32:
            key_plus = ord(char) + keyin
            if key_plus > 122:
                key_plus -= 26
            new_word += chr(key_plus)
        else:
            new_word += " "
    print('Ciphertext: "{}"' .format(new_word))

def check_word():
    word = input("Type the plaintext you want to encrypt.")
    if len(word) > 250:
        return None
    for char in word.lower():
        check = ord(char)
        if check == 32:
            continue
        if check >= 97 and check <= 122:
            continue
        return None
    return word

def check_key():
    keyin = int(input("Choose an input key. 0-25 or 100 for a random key."))
    if keyin >= 0 and keyin <= 25:
        return keyin

    if keyin == 100:
        keyin = random.randrange(26)
        print('Random key: {}' .format(keyin))
        return keyin

    return -1

def get_key():
    key = -1
    while key == -1:
        key = check_key()
    return key

def get_word():
    word = None
    while word == None:
        word = check_word()
    return word

def run_again():
    again = input("Again? (y/n)")
    while again.lower() != "y" and again.lower() != "yes" and again.lower() != "n" and again.lower() != "no":
        again = input("Again? (y/n)")
    if again.lower() == "y" or again.lower() == "yes":
        run()

def run():
    key = get_key()
    word = get_word()
    cipher(word,key)
    run_again()

run()
