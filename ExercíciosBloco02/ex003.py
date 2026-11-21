# Seno, Cosseno e Tangente de um ângulo, utilizando as funções radians, sin, cos e tan do módulo math.

from math import radians, sin, cos, tan
ang = float(input('Qual o valor do ângulo? '))
r = radians(ang)
s = sin(r)
c = cos(r)
t = tan(r)
print(' ' * 50)
print('O seno de {}° é igual a {:.2f}!'.format(ang, s))
print('O cosseno de {}° é igual a {:.2f}!'.format(ang, c))
print('A tangente de {}° é igual a {:.2f}!'.format(ang, t))
