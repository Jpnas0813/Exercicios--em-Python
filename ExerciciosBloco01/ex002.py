# Conversor de Medidas - Km, cm, mm

n1 = float(input('Diga o valor em metros a ser convertido: '))
print('{} metros é igual a {} km, {:.0f} cm e {:.0f} mm'.format(n1, n1/1000, n1*100, n1*1000))
