# Exercício 1

x = (((((12 * 3) + 4)// 10)* 5)- 2)
print(x)

# Exercicio 2 

x = 10 
y = 2

print(f" x + y = {x + y }") 
print(f" x * y = {x * y }")
print(f" x - y = {x - y }")
print(f" x // y = {x// y }")
print(f" x/ y = {x/ y}")
print(f" x % y = {x%y}")


# Exercício 3 

litros = area/6
galao = litros//18
lata = litros//4

if ((litros%4) !=0):
    lata+=1
if ((litros%18) !=0):
    galao+=1

if (litros <=12.8):
    galao_mistura, lata_mistura = 0, lata
else:
    galao_mistura = litros//18
    if((litros - litros//18)>= 12.8):
        galao_mistura, lata_mistura = galao_mistura+1,0
    else:
        lata_mistura = (litros - litros//18)//4
        if ((litros - litros//18)%4 !=0):
            lata_mistura +=1
