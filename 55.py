summa= 0
sana = 0
while True:
    n = int(input("enter a number : "))
    if n==0:
        break
    else:
        summa+=n
        sana+=1
print(f"sum:{summa//sana}")

#enter a number : 2
#enter a number : 5
#enter a number : 94
#enter a number : 28
#enter a number : 0
#sum:32
