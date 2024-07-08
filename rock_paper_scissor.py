import random
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
user_choice = (input("Pick a number:"))
pc_choice = random.randint(1,3)

#for printing computer emoji
if pc_choice == 1:
    print("You picked ✊")
elif pc_choice == 2:
    print("You picked ✋")
else:
    print("You picked ✌️")

# for printing user emoji
if user_choice == 1:
    print("CPU picked ✊")
elif user_choice == 2:
    print("CPU picked ✋")
else:
    print("CPU picked ✌️")

# for winning conditions of user
if user_choice == pc_choice:
    print("It's a tie")
elif user_choice == 1 and pc_choice == 3:
    print("You win")
elif user_choice == 2 and pc_choice == 1:
    print("You win")
elif user_choice == 3 and pc_chioce == 2:
    print("You win")
elif user_choice == 3 and pc_choice == 1:
    print("Computer win")
elif user_choice == 1 and pc_choice == 2:
    print("Computer win")
elif user_choice == 2 and pc_chioce == 3:
    print("Computer win")
else:
    print("You lose")
print("===================")
