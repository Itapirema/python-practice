km = float(input('Digite a velocidade do carro(Km): '))
if km > 80:
    print('Você está acima da velocidade permitida de 80Km/h. Terá que pagar uma multa de R${}'.format((km-80)*7))
else:
    print('Você esta dentro do limite permitido de 80Km/h')
