num1 = int(input('Informe um número \n'))
num2 = int(input('Informe um número \n'))
num3 = int(input('Informe um número \n'))

numsPrimos = 2
primoCurrent = 0
result = 1

while True:
    if num1%numsPrimos == 0:
        num1 = num1/numsPrimos
        primoCurrent = numsPrimos
    if num2%numsPrimos == 0:
        num2 = num2/numsPrimos
        primoCurrent = numsPrimos
    if num3%numsPrimos == 0:
        num3 = num3/numsPrimos
        primoCurrent = numsPrimos
    
    if primoCurrent == numsPrimos:
        if result == 1:
            result = 1 * primoCurrent
            primoCurrent = 0
        else:
            result = result * primoCurrent
            primoCurrent = 0
    else:
        numsPrimos = numsPrimos + 1
        while numsPrimos%2 == 0 and numsPrimos != 2:
            numsPrimos = numsPrimos+1
    if num1 == 1 and num2 == 1 and num3 == 1:
        print("MMC = ", result)
        break
    
