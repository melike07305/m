def gosmak():
    netije = san1 + san2
    print(f"Netije: {netije}")
def ayyrmak():
   san2 = int(input("Ikinji sanyny giriz"))
    san3 = int(input("ucunji sanyny giriz"))
    funksiya = input("Funksiyany saylan: +, -, *,/\nFunksiya:")
    if funksiya == "+":
        gosmak()
    elif funksiya == "-":
        ayyrmak()
    elif funksiya == "*":
        kopeltmek()
    elif funksiya == "/":
        bolmek()
    elif san3 == 0:
        bolmek_1()
    else:
        print("Nadogry funksiya")  netije = san1 - san2
    print(f"Netije: {netije}")
def kopeltmek():
    netije = san1 * san2
    print(f"Netije: {netije}")
def bolmek():
    netije = san1 / san2
    print(f"Netije: {netije}")
def bolmek_1(): 
    netije = san1/san3
    print(f"{netije} nola bolunenok")

while True:
    san1 = int(input("Birinji sanyny giriz"))
