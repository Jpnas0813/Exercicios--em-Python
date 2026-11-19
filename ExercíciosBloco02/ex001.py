# Entendendo o módulo math, em especial a função trunc e a função sqrt.

from math import trunc, sqrt
n = float(input('Digite um número de preferência decimal: '))
print(' ' * 50)
print('O valor {} tem como parte inteira {}.'.format(n, trunc(n)))
print('A raiz quadrada da parte inteira de {} é igual a {:.2f}!'.format(n, sqrt(trunc(n))))
print(' ' * 50)
