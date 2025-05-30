import random
'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([1 , -1 , 0])
ur_str = input("Enter Your Choice :")
ur_Dict = {
    "s" :1 , 
    "w" : -1,
    "g" : 0
}
reverse_Dict = {
    1 : "snake" , 
    -1 : "water" , 
    0 : "gun"
}
you = ur_Dict[ur_str]

print(f"You choose {reverse_Dict[you]}\n Compuetr choose {reverse_Dict[computer]}")

if (you == computer):
    print("Match draw !")
else :
    if (computer== 1 and you == -1):
        print("You Loss !")
    elif (computer == 1 and you == 0 ):
        print("You Loss !")
    elif(computer== -1 and you == 1):
        print("You Win !")
    elif(computer == -1 and you == 0 ):
        print("You Win !")
    elif(computer== 0 and you == 1):
        print("You Win !")

    elif (computer == 0 and you == -1):
        print("You Loss !")
    else :
        print("Something went wrong !")

    