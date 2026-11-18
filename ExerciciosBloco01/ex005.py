# Área da parede e quantidade de tinta necessária para pintá-la

h = float(input('Qual a altura da sua parede? '))
l = float(input('Qual a largura da sua parede? '))
área = h*l
tinta = área/2
print('Sua parede tem {}m² e você precisará de {:.2f}L de tinta para pintá-la.'.format(área, tinta))
