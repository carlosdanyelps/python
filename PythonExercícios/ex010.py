din = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = din / 5.06
eu = din / 5.36
ie = din / 0.034
print(f'Com R${din} você pode comprar US${dol:.2f}')
print(f'Com R${din} você pode comprar €{eu:.2f}')
print(f'Com R${din} você pode comprar ¥{ie:.2f}')

