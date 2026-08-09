import random
choices=["stone","paper","scissor"]
count=0
for i in range(3):
    player=input("choose stone,paper,scissor:")
    computer=random.choice(choices)
    print("Player:",player)
    print("Computer:",computer)
    if player==computer:
        print("draw")
    elif player=="stone" and computer=="scissor":
        print("you win")
        count+=1
    elif player=="scissor" and computer=="paper":
        print("you win")
        count+=1
    elif player=="paper" and computer=="stone" :
        print("you win")
        count+=1
    else:
        print("Computer win")
        
print("your wins count:",count)
if count>=2:
    print("Good job")
else:
    print("Try best")
print("game over")
