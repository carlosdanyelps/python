ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano % 4 == 0:
  print(f'O ano {ano} é BISSEXTO')
else:
  print(f'O ano {ano} não é BISSEXTO')
  