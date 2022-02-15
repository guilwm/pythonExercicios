#Exercício 28 do curso em vídeo
import random
from datetime import date
n1 = random.randrange(6)
#print(n1)
n2 = int(input("Digite um número: "))
if n1==n2:
    print('Você ganhou!')
else:
    print('Você perdeu!')

#Exercício 29 do curso em vídeo
v = int(input("Digite a velocidade do carro: "))
if v>80:
    print('Você foi multado! Sua multa custa R${} reais'.format((v-80)*7))

#Exercício 30 do curso em vídeo
n2 = int(input("Digite um número: "))
if n2 % 2 == 0:
    print('O número {} é par'.format(n2))
else:
    print('O número {} é ímpar'.format(n2))

#Exercício 31 do curso em vídeo
n2 = int(input("Digite a distância da viagem: "))
if n2 <= 200:
    print('O preço final da passagem é R${} reais'.format(n2*0.5))
else:
    print('O preço final da passagem é R${} reais'.format(n2 * 0.45))

#Exercício 32 do curso em vídeo
n2 = int(input("Digite o ano: "))
if n2 == 0:
    n2 = date.today().year
if (n2 % 4 == 0 and n2 % 100 != 0) or n2 % 400 == 0:
    print('O ano {} é bissexto!'.format(n2))
else:
    print('O ano {} nâo é bissexto!'.format(n2))