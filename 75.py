x = 1
a = int(input("Bir sany girizin: "))
if a < 0:
    print("Faktoriyal : Yalnys san! Pozitiw san girizin.")
else:
    for i in range(1,a + 1):
        x *= i
    print(f"Faktorial: {x}")

#Bir sany girizin: 3
#Faktorial: 6
