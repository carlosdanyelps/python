dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
carro = dias * 60
uso = 0.15 * km
print(f'O total a pagar é de R${carro+uso:.2f}')