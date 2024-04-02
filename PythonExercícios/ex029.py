#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velo = int(input('Informe a velocidade do carro: '))
if velo > 80:
  print('Você foi multado por dirigir acima de 80Km/h.')
else:
  print('Continue assim para evitar uma multa por alta velocidade.')