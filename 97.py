import random

def t():
    print("Sany biljek bolun! ")

    kici = int(input("in kici sany say;an:  "))
    uly = int(input("in uly sany say;an:  "))
    
    saylan = random.randint(kici,uly)
    s = 0

    while True:
        s += 1
        caklama = int(input("Sany caklan: "))

        if caklama > saylan:
            print("Sizin caklamanyz uly.")
        elif caklama< saylan:
            print("Sizin caklamanyz kici.")
        else:
            print(f"Dogry bildiniz {s} gezekden son")
            break
            
            
t()
