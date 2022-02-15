#Exercício 22 do curso em vídeo
nome = str(input('Digite seu nome: '))
print("Seu nome é: {}".format(nome))
print("Seu nome em maiúscula: {}".format(nome.upper()))
print("Seu nome em minuscula: {}".format(nome.lower()))
nome_fat = nome.split()#quebra uma string em várias menores
#print(len(nome))
#print(nome_fat)
print("O tamanho do primeiro nome é: {}".format(len(nome_fat[0])))
tam = len(nome_fat[0])+len(nome_fat[1])
print("O tamanho do nome completo sem espaços é: {}".format(tam))