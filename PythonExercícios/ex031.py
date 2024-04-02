
dist = int(input('Qual é a distância da viagem: '))
print(f'Vocé está prestes a começar uma viagem de {dist}Km.')

if dist <= 200:
   preco = dist * 0.50
else:
   preco = dist * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')
  
  