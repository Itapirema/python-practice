from random import randint
from time import sleep
nc = randint(0, 5)

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-'*20)
nu = int(input('Digite um numero: '))
print('PROCESSANDO...')
sleep(3)
if nc == nu:
    print('Acertou! O numero é {}'.format(nc))
else:
    print('Errou! O numero correto é {}, e não {}"'.format(nc, nu))
