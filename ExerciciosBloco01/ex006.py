# Preço com desconto

pr = float(input('Digite o preço do produto: R$'))
d = pr*0.05
f = pr-d
print('O produto terá um desconto de R${:.2f}, ficando com o preço final de R${:.2f}'.format(d, f))
