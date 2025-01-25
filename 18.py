fruits = {
    "alma":"8",
    "uzum" : "12",
    "hurma": "18",
    "banan" : "25",
    "nar" : "15"
}
k = 0
while True:
    fruit_name = input("Name almak isleyardiniz?")
    if fruit_name in fruits:
        kg = float(input("Nache kg almak isleyardiniz?"))
        k += kg * float(fruits[fruit_name])
    elif fruit_name == "quit":
        break
    else:
        print(f"There is no {fruit_name}")
print(f"Siz {k} manat tolemeli")
