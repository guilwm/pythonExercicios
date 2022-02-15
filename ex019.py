#Exercício 19 do curso em vídeo
import random

nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
random.shuffle(lista) #exercicio 20
print('O aluno escolhido foi {}!'.format(escolhido))
print('A ordem de apresentação dos alunos é: {}'.format(lista))