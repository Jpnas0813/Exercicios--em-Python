# Reajuste salarial de 15%

sl = float(input('Qual o salário a ser reajustado? R$'))
p = sl*0.15
aum = sl+p
print('O salário terá um aumento de R${:.2f}'.format(p))
print('O salário passará de R${:.2f} para R${:.2f}.'.format(sl, aum))
