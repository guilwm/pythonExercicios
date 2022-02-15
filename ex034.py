#Exercício 34 do curso em vídeo
n1 = int(input("Digite o salário do empregado: "))
if n1 <= 1250:
    sal = n1*(1+15 / 100)
else:
    sal = n1 * (1 + 10 / 100)

print("O salário reajustado do empregado é R${:.2f}".format(sal))

#Exercício 35 do curso em vídeo
n1 = int(input("Digite o primeiro lado: "))
n2 = int(input("Digite o segundo lado: "))
n3 = int(input("Digite o terceiro lado: "))

if((n1<n2+n3)and(n2<n1+n3)and(n3<n2+n1)):
    print('As retas podem formar um triangulo')
else:
    print('As retas não podem formar um triangulo')

