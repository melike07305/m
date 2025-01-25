Program = {
    "hello" : "Salam",
    "apple" : "alma",
    "water" : "suw",
    "bread" : "corek"
}
while True:
    x = int(input("Haysy program gerek: "))
    if x == 1:
        a = input("Enter a word in english: ")
        b = input("enter a word in turkmen: ")
        Program[a] = b
    if x == 2:
        for i,j in Program.items():
            print(f"{i} - {j}")
    if x == "exit":
        break
