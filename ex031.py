d = float(input('Qual é a distancia da viagem em Km? '))

if d <= 200:
    print('A passagem para uma viagem de {}Km é de R${}'.format(d, d*0.5))
else:
    print('A passagem para uma viagem de {}Km é de R${}'.format(d, d*0.45))
