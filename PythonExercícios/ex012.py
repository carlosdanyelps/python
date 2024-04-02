prod = float(input('Qual é o preço do produto? R$'))
desc = prod - (prod * 5 / 100)
print(f'O produto que custava R${prod}, na promoção com desconto de 5% vai custar R${desc:.2f}')
