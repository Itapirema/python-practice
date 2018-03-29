dias = int(input('Digite quantos dias de aluguel do veiculo: '))
km = float(input('Digite quanto Km foram percorridos pelo veiculo: '))
dp = dias * 60
kmp = km * 0.15
total = dp + kmp
print('O veiculo foi alugado por {} dias e rodou {}Km'.format(dias, km))
print('O total a pagar é de R${}'.format(total))
