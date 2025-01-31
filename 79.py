print('''
Jemi 10 sorag
''')
import random
jem1 = 0
jem2 = 0
for i in range(1,11):
    a = random.randint(1,30)
    b = random.randint(1,30)
    print(f'{i} - nji sorag\n {a} + {b} = ?')
    jogap = int(input('Your answer: '))
    if jogap == a + b:
        print('correct!!!!')
    jemi += 1
print('*** Your result ***')
print('Question: 10')
print(f'Correct answer: {jem1}')
print(f'Incorrect answer: {jem2}')
print(f'{jemi * 100 / 10}%')
