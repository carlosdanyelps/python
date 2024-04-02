'''Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

import math
ang = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))     
print(f'O ângulo de {ang} tem o SENO de {sen:.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {coss:.2f}')
print(f'O ângulo de {ang} tem o TANGENTE de {tan:.2f}')