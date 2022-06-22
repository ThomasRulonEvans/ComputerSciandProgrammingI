import random

def cipher(word,keyin):
    global done
    new_word = ""
    for char in word.lower():
        if ord(char) != 32:
            key_plus = ord(char) + keyin
            if key_plus > 122:
                key_plus -= 26
            new_word += chr(key_plus)
        if ord(char) == 32:
            new_word += " "
    print('Ciphertext: "{}"' .format(new_word))
    done = True


def check_word(word):
    check = 0
    if len(word) > 250:
        word = input("Type the plaintext you want to encrypt.")
        check_word(word)
    for char in word.lower():
        check = ord(char)
        if check != 32 and check < 97 or check != 32 and check > 122:
            word = input("Type the plaintext you want to encrypt.")
            check_word(word)
    if done != True:
        cipher(word,key)

def check_key(keyin):
    global key
    if keyin != 100 and keyin > 25 or keyin != 100 and keyin < 0:
        key = int(input("Choose and input key. 0-25 or 100 for a random key."))
        check_key(key)
    if keyin == 100:
        key = random.randrange(26)

def run():
    global key
    global word
    global yes
    global done
    done = False
    key = int(input("Choose and input key. 0-25 or 100 for a random key."))
    check_key(key)
    word = input("Type the plaintext you want to encrypt.")
    check_word(word)
    done = False
    yes = bool
    while yes != True or yes != False:
        again = input("Again? (y/n)")
        if again.lower() == "y" or again.lower() == "yes":
            yes = True
            run()
        if again.lower() == "n" or again.lower() == "no":
            yes = False
            break

run()


