def gosmak():
    netije = san1 + san2
    print(f"Netije: {netije}")
def ayyrmak():
    netije = san1 - san2
    print(f"Netije: {netije}")
def kopeltmek():
    netije = san1 * san2
    print(f"Netije: {netije}")

def bolmek():
    netije = san1 / san2
    print(f"Netije: {netije}")
while True:
    san1 = int(input("Birinji sanyny giriz"))
    san2 = int(input("Ikinji sanyny giriz"))
    funksiya = input("Funksiyany saylan: +, -, *,/\nFunksiya:")
    if san2 == 0 and funksiya == "/":
        print("bolup bolonok")
    elif funksiya == "+":
        gosmak()
    elif funksiya == "-":
        ayyrmak()
    elif funksiya == "*":
        kopeltmek()
    elif funksiya == "/":
        bolmek()
    else:
        print("Nadogry funksiya")
    
   
