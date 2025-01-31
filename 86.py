import random
computer = 0
player = 0
while True:
    m = input("Do you roll a dice? (yes/no) ")
    if m == "yes":
        computer2 = random.randint(1,6)
        player2 = random.randint(1,6)
        print(f"computer:{computer2}")
        computer += computer2
        print(f"computer:{player2}")
        player += player2
    else:
        break
print(" ***** Final Score *****")
print(f"comp: {computer}")
print(f"play: {player}")

