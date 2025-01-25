max_loop = int(input('Max loop: '))
space, star, loop = max_loop//2,1,1

while loop <= max_loop:
    print(space*''+ star * '*')
    
    if loop<= max_loop//2:
        space -=1
        star+=2
    else:
        space+=1
        star-=2
loop+=1
#false
