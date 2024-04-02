sal = int(input('Qual é o salário do funcionário? R$'))
if 1250 <= sal:
    aum = (sal / 100) * 10
else:
    aum = (sal / 100) * 15
print(f'Quem ganhava {sal}R$ passa a ganhar {sal + aum:.2f}R$')