nome = str(input('Digite um nome completo: '))
s = nome.split()
print('O primeiro nome é {} e o último nome é {}'.format(s[0], s[len(s) - 1]))
