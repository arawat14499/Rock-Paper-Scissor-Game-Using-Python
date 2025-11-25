import random
item_list = ["rock", "paper", "scissors"]

user_choice=input("enter your choice = Rock, Paper,scissors =")
comp_choice=random.choice(item_list)

print(f"user_choice = {user_choice}, comp_choice = {comp_choice}")

if user_choice==comp_choice:
    print("bothe choosen same: = Match tie")

elif user_choice=="Rock":
    if comp_choice=="paper":
        print("computer win")
    else:
        print("you win")

elif user_choice=="Paper":
    if comp_choice=="scissors":
        print("computer win")
    else:
        print("you win")

elif user_choice=="scissors":
    if comp_choice=="Rock":
        print("you win")
    else:
        print("computer win")
