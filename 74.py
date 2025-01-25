def numbers():
    sanlar = []
    while True:
        x = int(input("bir san girizin (Durmak ucin 0): "))
        if x == 0:
            break
        sanlar.append(x)
    return(f"in uly san: {max(sanlar)}, in kici san: {min(sanlar)}")


print(numbers())

#bir san girizin (Durmak ucin 0): 2
#bir san girizin (Durmak ucin 0): 3
#bir san girizin (Durmak ucin 0): 4
#bir san girizin (Durmak ucin 0): 5
#bir san girizin (Durmak ucin 0): 1
#bir san girizin (Durmak ucin 0): 0
#in uly san: 5, in kici san: 1
