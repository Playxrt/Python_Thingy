import random
mylist = [1, 2, 3]
rando = random.choice(mylist)

def RPC():
    print("Insert a number as per the following request")
    print("1 for Scissor")
    print("2 for Rock")
    print("3 for Paper")
    userinput = input("Insert num here->: ")
    if rando == 1:
        print("Computer chose scissor")
    elif rando == 2:
        print("Comoputer chose rock")
    elif rando == 3:
        print ("Computer chose paper")
    
    
    if userinput in ('1','2','3'):
        if userinput == '1':
            if rando == 1:
                print("Scissor is equal to scissor so draw")
            elif rando == 2:
                   print("Rock beats scissor so u lose")
            elif rando == 3:
                   print("Scissor beats paper so u win")
        elif userinput == '2':
            if rando == 1:
                print(" You win as rock beats scissor")
            elif rando == 2:
                print("Tie as rock is equal to rock")
            elif rando == 3:
                print("You lose as paper beats rock")
        elif userinput == '3':
            if rando == 1:
                print("You lose as scissor beats paper")
            elif rando == 2:
                print(" You win as paper beats rock")
            elif rando == 3:
                print(" Draw as paper is equal to paper")
    else:
        print("Give an accutual number given above")
RPC()
