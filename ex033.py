#Exercício 33 do curso em vídeo
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if(n1 > n2):
    aux1 = n1
    aux2 = n2
else:
    aux1 = n2
    aux2 = n1

if(n3 > aux1):
    max = n3
else:
    max = aux1

if(n3<aux2):
    min = n3
else:
    min = aux2

print('O menor número é {} e o maior número é {}.'.format(min, max))