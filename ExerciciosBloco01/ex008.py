# Á vista e parcelado

pr = float(input('Qual o valor do produto? R$'))
av = pr-(pr*0.1)
pc = pr+(pr*0.08)
print(' ' * 95)
print('O produto de valor R${:.2f}, terá a á vista um desconto de 10%, ficando no valor de R${:.2f}.'.format(pr, av))
print('Parcelado ele terá um aumento de 8%, ficando no valor de R${:.2f}.'.format(pc))
print(' ' * 95)
