import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotetuna vai medir {}'.format(hi))
print('A hipotetuna vai medir {}'.format(math.hypot(co, ca)))
