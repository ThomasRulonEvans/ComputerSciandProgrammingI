import random

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,50]

def play_standard_01(points,type):
    val = points
    nice = type
    make_throw(val,nice)

def make_throw(val,nice):
    nice_or = nice
    score = val
    tally = 0
    chance = random.randint(1,100)
    while score > 0:
        bust = False
        throw_ = random.choice(list)
        if throw_ > 0 and throw_ <= 20 and chance < 5:
            throw_ = throw_ * 3
            score -= throw_
            if nice_or == True:
                print("\n" + "cur score: " + str(score + throw_) + "\n" + "Throw: " + str(throw_) + "\n" + "Next score: " + str(score))
            elif nice_or == False:
                if score < 0:
                    bust = True
                print(str(score + throw_) + ", " + str(throw_) + ", " + str(score) + ", " + str(bust))
            if score < 0:
                if nice_or == True:
                    print("You bust!")
                score += throw_
            tally += 1
        elif throw_ > 0 and throw_ <= 20 and chance < 10:
            throw_ = throw_ * 2
            score -= throw_
            if nice_or == True:
                print("\n" + "cur score: " + str(score + throw_) + "\n" + "Throw: " + str(throw_) + "\n" + "Next score: " + str(score))
            elif nice_or == False:
                if score < 0:
                    bust = True
                print(str(score + throw_) + ", " + str(throw_) + ", " + str(score) + ", " + str(bust))
            if score < 0:
                if nice_or == True:
                    print("You bust!")
                score += throw_
            tally += 1
        else:
            score -= throw_
            if nice_or == True:
                print("\n" + "cur score: " + str(score + throw_) + "\n" + "Throw: " + str(throw_) + "\n" + "Next score: " + str(score))
            elif nice_or == False:
                if score < 0:
                    bust = True
                print(str(score + throw_) + ", " + str(throw_) + ", " + str(score) + ", " + str(bust))
            if score < 0:
                if nice_or == True:
                    print("You bust!")
                score += throw_
            tally += 1
    if nice_or == True:
        print(str(tally)+" throws required for " +str(val) + " score")
