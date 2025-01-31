def cafe_system():
    print("Welcome to the Cafe")
    Menu = {
        "Coffee" : {"category" : "(drinks)","price" : 3},
        "Tea" : {"category" : "(drinks)","price" : 2}, 
        "Sandwich" : {"category" : "(food)","price" : 5}, 
        "Cake" : {"category" : "(deserts)","price" : 4},
    }
    jem = 0
    while True:
        print("\nmenu:")
        for i,j in Menu.items():
            print(f"{i} {j['category']} : {j['price']} $")
        ask = input("enter the item you want to order or 'done': ")
        if ask in Menu:
            quantity = int(input("Enter the quantity: "))
            print(f"{quantity} {ask} (s) added to your order")
            cost = Menu[ask]["price"] * int(quantity)
            jem += cost
        elif ask == "done":
            print(f"\n{ask}x{quantity}:{cost}$")
            break
    print(f"\nTotal amount: {jem}$")
    print("Thank you for your order")
cafe_system()



