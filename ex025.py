#Exercício 25 do curso em vídeo
nome = str(input('Digite o nome do usuário: ')).strip()
nomeaux = nome.upper()
print(nomeaux.find('SILVA') != -1)

#Exercício 26 do curso em vídeo
nome = str(input('Digite uma frase: ')).strip().upper()
nomeaux = nome
print('A frase possui {} letras A'.format(nomeaux.count('A')))
print('A letra A aparece inicialmente na posição {} '.format((nomeaux.find('A')+1)))
print('A letra A aparece por último na posição {}'.format((nomeaux.rfind('A')+1)))

#Exercício 27 do curso em vídeo
nome = str(input('Digite o nome do usuário: ')).strip()
nomeaux = nome.split()
print('O primeiro nome do usuário é: {}'.format(nomeaux[0]))
print('O último nome do usuário é: {}'.format(nomeaux[len(nomeaux)-1]))
