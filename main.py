import random

again = True

dice = int(input("Number of Dice -> "))

while again:
    # print(random.randint(1,6))
    for i in range(1,dice+1):
        print(random.randint(1,6),end=' ')
    print()
    roll_again = input("Roll ? (y/n) -> ")

    if roll_again.lower() == 'y':
        continue
    else:
        break