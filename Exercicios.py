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

area = int(input('Digite o tamanho em metros quadrados da área a ser pintada: '))

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

print(f'Litros necessários para a pintura: {litros} litros\nComprando apenas galões: {galao} galões de 18 litros, que totalizam {galao*18} litros\nComprando apenas latas: {lata} latas de 4 litros, que totalizam {lata*4} litros.\nComprando latas e galões misturados: {lata_mistura} latas de 4 litros e {galao_mistura} galões de 18 litros, que totalizam {4*lata_mistura + 18*galao_mistura} litros.')


# Exercicio 4

n = int(input("Digite o valor de n: "))

cont, soma = 2, 1
while cont < n:
    if n % cont == 0:
        soma += cont
    cont += 1

if soma == n:
    print ("O número", n, "é perfeito")
else:
    print ("O número", n, "não é perfeito")


# Exercicio 5

m = int(input("Digite o valor de m: "))
for n in range(1, m+1):
    soma, inicio = 0, 1
    while soma != n*n*n:
        soma = 0
        for i in range(n):
            soma = soma + inicio + 2 * i
        inicio += 2

    inicio = inicio - 2
    print("%d*%d*%d = " % (n, n, n))
    for i in range(n):
        print("+", inicio + 2 * i)
    print("\n")


# Exercicio 6

num = 37

chutes = 0

print("Tente advinhar o número que eu estou pensando")

while True:
    chute = int(input("Seu Chute: "))
    chutes += 1
    if chute == num:
        break
    elif chute < num:
        print("Você deve chutar mais alto!")
    else:
        print("Você deve chutar mais baixo!")


print("Parabens você acertou!!")
print("Você chutou %i vezes"%chutes)

# Exercicio 7

altura = float(input("Digite a sua altura: "))
sexo = int(input("Digite o seu sexo(Masculino = 0/ Feminino = 1): "))
peso = float(input("Digite o seu peso: "))

if sexo == 0:
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

if peso > peso_ideal:
    print("Você está acima do peso")
elif peso == peso_ideal:
    print("Você está no seu peso ideal")
else:
    print("Você está abaixo do peso")


# Exercicio 8 

notas = []

while True:
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    if nota == -1: break

print("Foram lidos %i valores." % len(notas))

print("\nValores informados: ")
for nota in notas:
    print(nota)

print("\nValores informados (ordem inversa): ")
notas.reverse()
for nota in notas:
    print(nota)

soma = 0
for nota in notas:
    soma += nota
print("\nA soma de valores é", soma)

soma /= len(notas)
print("\nA média dos valores é", soma)

acima = 0
for nota in notas:
    if nota > soma:
        acima += 1
print("\nNúmero de notas acima da média é", acima)

abaixo = 0
for nota in notas:
    if nota < 7:
        abaixo += 1
print("\nNúmero de notas abaixo de 7 é", abaixo)

# Exercicio 9 

nomes = []
agenda = {}

while True:
    ordem = input('Deseja adicionar um novo contato(add) ou parar a execução(stop)').lower()

    if not ordem.isalpha():
        print("Digite apenas letras!")
        
    elif ordem.startswith('a'):
        contato = {}


        nome = input('Digite o nome do contato: ')
        if not nome[0].isupper():
            nome = nome[0].upper() + nome[1:]

        nomes.append(nome)

        tel = input('Digite o telefone do contato: ')
        contato['Telefone'] = tel

        end = input('Digite o endereço do contato: ')
        contato['Endereço'] = end

        email = input('Digite o Email do contato: ')
        contato['Email'] = email

        agenda[nome] = contato
        
    elif ordem.startswith('s'):
        break

print('A G E N D A\n')
nomes.sort()
for nome in nomes:
    print('Nome: ', nome)
    print('Telefone: ', agenda[nome]['Telefone'])
    print('Endereço: ', agenda[nome]['Endereço'])
    print('Email: ', agenda[nome]['Email'])
    print()

# Exercicio 10 

TAM_MAX_CH = 26

# primeiro nós pegamos o modo a ser aplicado na string
while True:
    modo = input("Você deseja criptografar ou decriptografar? ").lower()
    if modo in ["criptografar", "c", "decriptografar",  "d"]:
        break
    else:
        print("Entre 'criptografar' ou 'c' ou 'decriptografar' ou 'd'.")

# depois pedimos a mensagem a ser processada
mensagem = input("Entre sua mensagem: ").lower()

# garante que a mensagem não tenha caractéres com acento ou ç
orig = "áàãâéèêíìîóòõôúùûç"
sub = "aaaaeeeiiioooouuuc"
repl = dict(zip(orig, sub))
for o, r in repl.items():
    mensagem = mensagem.replace(o, r)

# pedimos então a chave da criptografia
chave = 0
while True:
    chave = int(input(f"Entre o número da chave (1-{TAM_MAX_CH}): "))
    if 1 <= chave <= TAM_MAX_CH:
        break
    else:
        print(f"A chave deve estar entre 1 e {TAM_MAX_CH}")
        
# Nós então traduzimos a mensagem
if modo[0] == "d":
    chave *= -1

traduzido = ""

# para cada caracter na mensagem
for simbolo in mensagem:
    # nós verificamos se o caracter é alpha numérico
    if simbolo.isalpha():
        # se for nós pegamos a ordem do simbolo
        num = ord(simbolo)
        
        # então nós adicionamos o valor da chave a ordem
        num += chave
        
        # nós então garantimos que o simbolo não ultrapasse os
        # valores de ordem entre A e Z
        if num > ord("z"):
            num -= 26
        elif num < ord("a"):
            num += 26
        
        # convertemos o simbolo para um caracter e adicionamos
        # a mensagem
        traduzido += chr(num)
    else:
        traduzido += simbolo

# imprime a mensagem traduzida
print(traduzido)

# Exercicio 11

import random

print("Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!")

porta = int(input("Escolha uma porta: "))
# premio = random.choice([1, 2, 3])
# premio = random.randrange(1, 4)
premio = random.randint(1, 3)

if premio != 1 and porta != 1:
    bode = 1
elif premio != 2 and porta != 2:
    bode = 2
else:
    bode = 3

print("Você escolheu a porta %i, mas" % porta)
print("eu lhe informo que na porta %i há um bode." % bode)

decisão = int(input("Deseja trocar de porta (1 - Sim/ 0 - Não): "))

if decisão == 1:
    if porta != 1 and bode != 1:
        porta = 1
    elif porta != 2 and bode != 2:
        porta = 2
    else:
        porta = 3

if porta == premio:
    print("Ganhou um carro!")
else:
    print("Não ganhou um carro...")

