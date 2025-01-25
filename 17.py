dictionary = {
        "hello":"salam",
        "apple":"alma",
        "lemon":"limon",
        "cat":"pishik",
        "dog":"it",
        "flag":"baydak",
        "student":"okuwcy",
        "family":"mashgala",
        "pen":"ruchka",
        "water":"suw",
        "bread":"corek"
    }
while True:
    print("""***** MY DICTIONARY PROGRAM *****
    
    1.Show
    2.Add
    3.Edit
    4.Delete
    5.Exit
    """)

    your_choise = int(input("Your choise?"))
    if your_choise == 1:
        for i, j in dictionary.items():
            print(f"{i} - {j}")
    elif your_choise == 2:
        english = input("Enter the word in English: ")
        turkmen = input("Enter the word in turkmen: ")
        dictionary[english] = turkmen
        print("Added\n")
    elif your_choise ==3:
        english = input("Enter the word in English: ")
        turkmen = input("Enter the word in turkmen: ")
        dictionary[english] = turkmen
        print("Edited\n")
    elif your_choise == 4:
        english = input("Enter the word in Ebglish: ")
        dictionary.pop(english)
        print("Deleted\n")
    else:
        break
