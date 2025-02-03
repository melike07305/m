import random
A = ["picture", "number"]
a = 0
b = 0
for i in range(1, 11):
    rand = random.choice(A)
    print(i, rand)
    if rand == 'number':
        a += 1
    else:
        b += 1
print(f"NUMBER: ", a)
print(f"PICTURE: ", b)
if a > b:
    print("Most tossed NUMBER")
elif a < b:
    print("Most tossed PICTURE")
else:
    print("Equal!!")
