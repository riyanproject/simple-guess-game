import random

toprange=input("type a num")

if toprange.isdigit():
    toprange=int(toprange)

    if toprange<=0:
        print("pls enter a a num greater than 0")
        quit()
else:
    print("pls enter a num next time")
    quit()

randomn=random.randint(0,toprange)
guesses=0

while True:
    guesses+=1
    userguesses=input("make a guess:")
    if userguesses.isdigit():
        userguesses=int(userguesses)
    else:
        print("pls enter a num next time")
        continue

    if userguesses==randomn:
        print("you got it")
        break
    elif userguesses>randomn:
        print("you were above the number")
    else:
        print("you are below the number")

print("you got it in",guesses,'guesses')