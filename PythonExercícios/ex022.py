 #Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre: – O nome com todas as letras maiúsculas e minúsculas. – Quantas letras ao todo (sem considerar espaços). – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))

print(f'Seu nome em maiúsculo: {nome.upper()}')

print(f'Seu nome em minúsculo: {nome.lower()}')

nome = nome.strip()
print("Seu nome tem ao todo {} carácteres.".format(len(nome) - nome.count(' ')))

print(f'Seu primeiro nome tem {nome.find(" ")} Caracteres.')
