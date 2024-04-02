#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

city = input('Informe o nome de uma cidade: ').strip()

print(city[:5].upper() == 'SANTO')