'''rock,paper,scissor, game where user have to put their 
choice as 'r' for 'rock' , 'p' for 'paper' and 's' for 
scissor.'''
import random
choices=[0,1,-1]
computer=random.choice(choices)
you=input("Enter you choice: 's' for scissor, 'p' for paper and 'r' for 'rock'.:\n ")
dictionary={"s":1, "p":0, "r":-1}
youdict=dictionary[you]
reversdict={1:"scissor", 0:"paper", -1:"rock"}
print(f"you choose:{reversdict[youdict]} and computer choose:{reversdict[computer]}")
if (computer==youdict):
    print("game is draw!")
else:
    if(computer==0 and youdict==1):
        print("you wins!")
        print("congrats")
    elif(computer==1 and youdict==0):
        print("you loose!")
        print("try again")
    elif(computer==-1 and youdict==0):
        print("you loose!")
        print("try again ")
    elif(computer==0 and youdict==-1):
        print("you wins!")
        print("congrats")
    elif(computer==1 and youdict==-1):
        print("you loose!")
        print("try again")
    elif(computer==-1 and youdict==1):
        print("you wins!")
        print("congrats")
    