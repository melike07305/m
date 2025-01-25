telefon_belgi = {"Anna" : "63188199",
                "Gurban" : "63115599",
                "Oraz" : "62111444",}

print(telefon_belgi)
print(telefon_belgi["Anna"])
A = input("Kimin telefon belgisi gerek?")
if A in telefon_belgi:
    print(telefon_belgi[A])
else:
    print(f"{A} - yn telefon tapylmady")
print(len(telefon_belgi))
telefon_belgi["Gurban"] = "63625495"
print(telefon_belgi)
telefon_belgi["Muhammet"] = "63384289"
print(telefon_belgi)
telefon_belgi.pop("Gurban")
print(telefon_belgi)
for i in telefon_belgi:
    print(i)
for i in telefon_belgi:
    print(telefon_belgi[i])
for i in telefon_belgi:
    print(f"{i} {telefon_belgi[i]}")
telefon_belgi.clear()
print(telefon_belgi)
