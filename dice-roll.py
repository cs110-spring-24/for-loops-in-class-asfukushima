# 2/12/24
import random
# lets simulate roll 100 dice and print out each die value
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for roll in range(100):
    dice = random.randint(1, 6)
    if dice == 1:
        print("1")
        one += 1
    elif dice == 2:
        print("2")
        two += 1
    elif dice == 3:
        print("3")
        three += 1
    elif dice == 4:
        print("4")
        four += 1
    elif dice == 5:
        print("5")
        five += 1
    else:
        print("6")
        six += 1
print(f"after 100 dice rolls, we rolled {one} ones, {two} twos, {three} threes, {four} fours, {five} fives, and {six} sixes")
# now lets count how many 1,2,3,4,5,6 were rolled.
