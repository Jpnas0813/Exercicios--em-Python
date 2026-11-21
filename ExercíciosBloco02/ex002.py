# Cálculo da hipotenusa de um triângulo retângulo, utilizando a função pow e sqrt do módulo math.

from math import pow, sqrt
a = float(input('Qual o valor do primeiro cateto? '))
b = float(input('Qual o valor do segund cateto? '))
c = sqrt(pow(a, 2) + pow(b, 2))
print(' ' * 50)
print('O valor da hipotenusa com catetos de {:.2f} e {:.2f} é igual a {:.2f}!'.format(a, b, c))
