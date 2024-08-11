##Project - "Guess The Number"
#First we will import "Random" module
import random
print('''Welcome To game GUESS THE NUMBER''')
guess_num =random.randint(1,100)
user = int(input("Press 1 To Start\n"))
i = 0
while(user > guess_num or user < guess_num):
    user = int(input("Guess the number between (1,100)\n"))
    if(user > guess_num):
        i +=1
        print("You have Guessed Too High,",i,"th chance")
    elif(user < guess_num):
        i +=1
        print("You have Guesssed Too Low,",i,"th chance")
if(user == guess_num):
    print("Congratulations, You have won")        
    z = input("Press Enter to exit")
 