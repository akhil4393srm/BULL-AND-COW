import random
rn=random.randint(1000,9999)
listnum=str(rn)
#print(rn)
count=0
while True:
    
    count+=1
    print(count,"trail")
    guess = input("ENTER YOUR 4 DIGIT NUMBER: ")
    
    if guess == listnum:
        print("You won.")
        print("It took you "+str(count)+" guess(es).")
        break

    else:
        cow=0
        bull=0
        for x in range(0,4):
            if guess[x]==listnum[x]:
                cow += 1
            elif guess[x] in listnum: # look if digit is somewhere else in the solution key (might already be a cow)
                bull += 1
    print("Cows: "+str(cow)+" Bulls: "+str(bull))
    print("++++++++++++++++")
