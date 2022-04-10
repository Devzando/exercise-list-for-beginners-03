import random

num1 = 0
num2 = 0
num3 = 0
stop = True
x=0

while stop:
    num1 = random.randint(0, 200) 
    num2 = random.randint(0, 200) 
    num3 = random.randint(0, 200)

    if num1 == num2 and num1 == num3:
        print(num1, num2, num3)
        print('Foram precisos gerar', x, 'trios')
        stop = False
    else:
        num1 = random.randint(0, 200) 
        num2 = random.randint(0, 200) 
        num3 = random.randint(0, 200)
        x+=1

