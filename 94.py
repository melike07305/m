import random

print('''
Jemi 10 sorag
''')

jem1 = 0
jem2 = 0

for i in range(1,11):
    a = random.randint(1,30)
    b = random.randint(1,30)
    operation = random.choice(['*','-'])

    if operation  == '*':
        print(f"{i} - mji sorag\n{a} + {b} =?")
        correct_answer = a + b
    else:
        print(f"{i} nji sorag\n{a} - {b} =?")
        correct_answer = a - b 
    jogap = int(input('Your answer: '))

    if jogap == correct_answer:
        print('corect!!!!!!')
        jem1 += 1
    else:
        print(f"Your answer is incorrect! Correct answer is {correct_answer}")
        jem2 += 1

print('*** Yoour result ***')
print('Question: 10')
print(f'Correct answer: {jem1}')
print(f'inCorrect answer: {jem2}')
print(f'{jem1 * 100/10} %')
