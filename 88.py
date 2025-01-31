import random
A = ["picture", "number"]
m = 0
n = 0
for i in range(0,10):
    rand = random.choice(A)
    print(i,rand)
    if rand == "picture":
        m += 1
    else:
        n += 1
print(f"number: ",m)
print(f"picture: ",n)
if n < m:
    print("most tossed number")
else:
    print("most tossed picture")
  
