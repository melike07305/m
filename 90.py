a = [18,42,600,214,86,320,99,52,901]
two_bel = []
three_bel = []
muk_1 = 0
muk_2 = 0
for i in a:
    if i <100:
        two_bel.append(i)
        muk_1 += i
    elif 99 < i < 1000:
        three_bel.append(i)
        muk_2 += i
print(f"{two_bel} \n mukdar: {muk_1} \n")
print(f"{three_bel} \n mukdar: {muk_2} \n")
