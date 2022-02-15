# exercício 8 do Curso em Vídeo de Python
medida = float(input('Digite uma medida em metros: '))
print('A conversão de {} é:'.format(medida))
print('{} km'.format(medida*0.001))
print('{:.3f} hm'.format(medida*0.01))
print('{:.3f} dam'.format(medida*0.1))
print('{} dm'.format(medida*10))
print('{} cm'.format(medida*100))
print('{} mm'.format(medida*1000))


# exercício 9 do Curso em Vídeo de Python
n1 = int(input('Entre com um número: '))
print('-'*25)
print('A tabuada do número {} é: '.format(n1))
print('{}x 1 =  {}'.format(n1,(n1*1)))
print('{}x 2 =  {}'.format(n1,(n1*2)))
print('{}x 3 =  {}'.format(n1,(n1*3)))
print('{}x 4 =  {}'.format(n1,(n1*4)))
print('{}x 5 =  {}'.format(n1,(n1*5)))
print('{}x 6 =  {}'.format(n1,(n1*6)))
print('{}x 7 =  {}'.format(n1,(n1*7)))
print('{}x 8 =  {}'.format(n1,(n1*8)))
print('{}x 9 =  {}'.format(n1,(n1*9)))
print('{}x10 =  {}'.format(n1,(n1*10)))
print('-'*25)

# exercício 10 do Curso em Vídeo de Python
real = float(input('Digite seu saldo: '))
dolar = real/5.40
print('Com R${} você consegue comprar US${} dólares'.format(real, dolar))

# exercício 11 do Curso em Vídeo de Python
lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar*alt
tinta = area/2
print('A área total da parede é: {}m²'.format(area))
print('A quantidade de tinta usada é de {} litros'.format(tinta))

# exercício 12 do Curso em Vídeo de Python
preco = float(input('Digite o preço do produto: '))
npreco = (1-0.05)*preco
print('O novo preço do produto com 5% de desconto é: {:.2f}'.format(npreco))