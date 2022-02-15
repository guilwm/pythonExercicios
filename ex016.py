#Exercício 16 do curso em vídeo
import math
real = float(input('Digite um número: '))
print('A parte inteira do número {} é {}'.format(real, math.floor(real)))

#Exercício 17 do curso em vídeo
cat1 = float(input('Digite o cateto oposto do triângulo: '))
cat2 = float(input('Digite o cateto adjacente do triângulo: '))
#hip = math.sqrt(cat1**2+cat2**2)
hip = math.hypot(cat1, cat2)
print('A hipotenusa do triângulo é {:.2f}'.format(hip))

#Exercício 18 do curso em vídeo
ang = float(input('Digite um ângulo em graus '))
print('O seno de {} é {:.3f}'.format(ang, math.sin(math.radians(ang))))
print('O cosseno de {} é {:.3f}'.format(ang, math.cos(math.radians(ang))))
print('A tangente de {} é {:.3f}'.format(ang, math.tan(math.radians(ang))))