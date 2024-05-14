import random
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
int(input("Pick a number:"))
int_pc = random.randint(1,3)

#for printing computer emoji
if int_pc == 1:
    print("You picked ✊")
elif int_pc == 2:
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
if int == int_pc:
    print("It's a tie")
elif int == 1 and int_pc == 3:
    print("You win")
elif int == 2 and int_pc == 1:
    print("You win")
elif int == 3 and int_pc == 2:
    print("You win")
else:
    print("You lose")
print("===================")