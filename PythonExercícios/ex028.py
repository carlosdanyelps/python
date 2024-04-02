#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
n_a = random.randint(1,5)
n1 = int(input('Tente acertar o número, Informe um número de 1 a 5: '))
if n1 == n_a:
  print('VOCÊ VENCEU!')
else:
  print('VOCÊ PERDEU!')
