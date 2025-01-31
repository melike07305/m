y = 0
z = 0
def python(y,z):
    a = input("Soz yazyn: ")
    for i in a:
        if i.isupper():
            y += 1
        elif i.islower():
            z += 1
    print(f"Uly harplaryn sany: {y}")
    print(f"Kici harplaryn sany: {z}")
python(y,z)

#Soz yazyn: Gujurly Nesil
#Uly harplaryn sany: 2
#Kici harplaryn sany: 10
