okuwcy = {
    "Agos" : 110,
    "Alpi" : 100,
    "Bega" : "A+",
    "Ata" : 99,
    "Melike" : 100}
a = input("Student: ")
if a in okuwcy:
    print(f"{a} - nyn baly {okuwcy[a]}")
else:
    print("Sorry ol okuwcy bizde yok")

# Student: Melike
# Melike - nyn baly 100
# Student: Gulperi
# Sorry ol okuwcy bizde yok
