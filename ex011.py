largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura;
print('Sua parede tem {}x{} e sua aárea é de {:.2f}m²'.format(largura, altura, area))
tinta = area / 2
print('Para pintar a parede você precisará de {:.2f}l de tinta'.format(tinta))

