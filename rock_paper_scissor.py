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
if int == 1:
    print("CPU picked ✊")
elif int == 2:
    print("CPU picked ✋")
else:
    print("CPU picked ✌️")

# for winning conditions
if int == pc_choice:
    print("It's a tie")
elif int == 1 and pc_choice == 3:
    print("You win")
elif int == 2 and pc_choice == 1:
    print("You win")
elif int == 3 and pc_chioce == 2:
    print("You win")
else:
    print("You lose")
print("===================")
