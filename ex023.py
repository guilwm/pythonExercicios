#Exercício 23 do curso em vídeo
num = input('Digite um numero entre 0 e 9999 ')
print('Os dígitos do número são: {},{},{},{}'.format(num[0], num[1], num[2], num[3]))

num2 = int(input('Digite um numero entre 0 e 9999 '))
milhar = num2//1000
aux1 = num2%1000
cent = aux1//100
aux2 = aux1%100
dez = aux2//10
uni = aux2%10
print('O dígito de milhar é {}'.format(milhar))
print('O dígito de centena é {}'.format(cent))
print('O dígito de dezena é {}'.format(dez))
print('O dígito de unidade é {}'.format(uni))