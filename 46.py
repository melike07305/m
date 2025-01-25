phone = int(input("enter your phone number: "))
total_paid =0
while True:
    payment = input("please pay: ")
    if payment == 'quit':
        break
    else:
        total_paid += int(payment)
        print(f" you paid {total_paid} manats")
print(f"{total_paid} manats were transfered to {phone}")


#enter your phone number: +99361248129
#please pay: 10
# you paid 10 manats
#please pay: 0
# you paid 0 manats
