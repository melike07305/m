passed = 0
total = 0
passing= 50
while True:
    score = input("enter student score: ")
    if score =="quit":
        break
    total +=1
    if int(score)>= passing:
        passed +=1
if total> 0:
    percent = (passed/total) *100
    print(f"{percent}% of students passed the exam.")
else:
    print("no students took the exam.")

#enter student score: 34
#enter student score: 57
#enter student score: 90
#enter student score: 69
#enter student score: 42
#enter student score: 72
#enter student score: quit
#66.66666666666666% of students passed the exam.
