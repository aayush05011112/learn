import random
targetnum=random.randint(1,100)
while True:
    userint=input("Enter the guess number or press(Q) to quit:")
    if(userint=="Q"):
        break
    int(userint)
    if(targetnum==int(userint)):
        print("You have guessed the number correctly")
        break
    if(targetnum>int(userint)):
        print("Your guessed number is low guess higher")
    elif(targetnum<int(userint)):
        print("Your gussed number is higher then the target guess lower")
print("----Game over----")