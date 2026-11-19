# Aluguel de Carros - Dia e Km rodado

dia = int(input('Qual a quantidade de dias alugados? '))
km = float(input('Qual a quantidades de km rodados? '))
pdia = dia*60
pkm = km*0.15
print(' ' * 50)
print('Alugando o carro por {} dias e percorrendo {} km, o saldo devedor é igual a R${:.2f}.'.format(dia, km, pdia+pkm))
print('Valor do dia = R${:.2f}'.format(pdia))
print('Valor do km = R${:.2f}'.format(pkm))
