# exercício 13 do Curso em Vídeo de Python
sal = float(input('Digite o salário do empregado: '))
nsal = sal*(1+(15/100))
print('O novo salário do empregado com reajuste de 15% é: {:.2f}'.format(nsal))

# exercício 14 do Curso em Vídeo de Python
tempc = float(input('Digite a temperatura em °C: '))
temph = tempc*9/5 + 32
print('A temperatura de {}°C é {}°F Fahrenheit'.format(tempc, temph))

# exercício 15 do Curso em Vídeo de Python
dist = float(input('Digite a distância percorrida pelo carro '))
dia = int(input('Digite a quantidade de dias que o carro ficou alugado '))
preco = dist*0.15 + dia*60
print('O total a pagar pelo aluguel do carro é: R${} reais'.format(preco))