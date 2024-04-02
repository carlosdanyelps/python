salário = float(input(f'Qual o salário do Funcionário? R$'))
aumento = salário + (salário * 15 / 100)
print(f'Um funcionário que ganhava R${salário}, com 15% de aumento, passa a receber R${aumento:.2f}')
