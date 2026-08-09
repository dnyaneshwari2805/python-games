import random
number=random.randint(1,10)

for i in range(3):
    guess=int(input("enter the number:"))
    if guess==number:
        print("correct")
        print("Congratulations")
        break
    elif guess<number:
        print("Too low")
    else:
        print("Too high")
else:
    print("Game over!")
    print("You used all 3 chances")
print("Correct number is:",number)
