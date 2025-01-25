total = 0
count = 0
while True:
    num = input("enter a number: ")
    if num == "quit":
        break
    total+= int(num)
    count+= 1

if count>0:
    average= total/count
    print("average:", average)
else:
    print("you haven't etered any numbers.")

#enter a number: 22
#enter a number: 5
#enter a number: 94
#enter a number: 28
#enter a number: quit
#average: 37.25
