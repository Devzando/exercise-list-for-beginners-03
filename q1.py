import random

par1 = 0
parMenor = 0
impar1 = 0
imparMaior = 0

for i in range(1, 51):
    a=random.randint(0, 100)
    b=random.randint(0, 100)

    if a%2 == 0 and b%2 == 0:
        if a>b:
            par1 = a
            parMenor = b
        else: 
            par1 = b
            parMenor = a
    if a%2 == 0 and b%2 == 1:
        par1 = a
        impar1 = b
    else:
        par1 = b
        impar1 = a
    if a%2 == 1 and b%2 == 1:
        if a>b:
            impar1 = b
            imparMaior = a
        else:
            impar1 = a
            imparMaior = b

print('Pares', par1, " ", parMenor)
print('Impares', impar1, " ", imparMaior)
        