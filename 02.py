# Soraglar we dogry jogaplar bilen bir sanaw
soraglar = [
    ("Gujurly nacinji yylda acyldy?", ["2017", "2010", "1999", "2014"], "2014"),
    ("Gujurlyn SMM-my kim?", ["Resul Nuryyev", "Atajan Atayev", "Ayna Esenova", "Agabay Agabayev"], "Ayna Esenova"),

    ("Soraglary ozum tapdymmy?", ["yok", "hovo", "munkun", "belki"], "hovo")
]

# Başlangyç baly
bal = 0
dogry_jogap_sany = 0
yalnys_jogap_sany = 0
sorag_sany = 0  # Soraglaryň sanyny hasaplamak üçin
sorag_sany = 0  

# 10 sorag sorandan soň oýuny tamamlap, netije görkezýän döngü
for sorag in soraglar:
    # Soraglary görkezeris
    
    print(f"Sorag: {sorag[0]}")
    jogaplar = sorag[1]  # Jogaplar sanawy
    dogry_jogap = sorag[2]  # Dogry jogap
    jogaplar = sorag[1] 
    dogry_jogap = sorag[2]  

    # Jogaplary görkezýäris (1-den başlaýan nomerler bilen)
    
    print(f"1. {jogaplar[0]}")
    print(f"2. {jogaplar[1]}")
    print(f"3. {jogaplar[2]}")
    print(f"4. {jogaplar[3]}")

    # Ulanyjynyň jogabyny alýarys
    
    ulanyjy_jogaby = int(input("Jogabyňyzy saýlaň (1-4): ")) - 1

    # Jogabynyň dogrylygyny barlaýarys
    
    if jogaplar[ulanyjy_jogaby] == dogry_jogap:
        print("Dogry jogap!")
        bal += 10  # Dogry jogap üçin 10 bal goşýarys
        bal += 10  
        dogry_jogap_sany += 1
    else:
        print(f"Ýalňyş jogap! Dogry jogap: {dogry_jogap}")
        bal -= 5  # Ýalňyş jogap üçin 5 bal aýyrýarys
        bal -= 5  
        yalnys_jogap_sany += 1

    sorag_sany += 1  # Soraglaryň sanyny hasaplaýarys
    sorag_sany += 1  
    

    # Eger 10 sorag soralan bolsa döngini bozýarys
    if sorag_sany == 10:
        break

    print()  # Bir setir boş ýer goýýarys
    print()  

# Oýnuň soňunda jemleýji netije
print("")
print(f"Oýun tamamlandy! 🎉🎊🎈🎇🎆✨✨🎉 \nJemi bal: {bal}")
print(f"Dogry jogaplaryň sany: {dogry_jogap_sany}")
