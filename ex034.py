s = float(input('Informe seu salário: R$'))
if s > 1250:
    print("O novo salário com aumento será de R${}".format((s * 10 / 100) + s))
else:
    print('O salário com aumento será de R${}'.format((s * 15 / 100) + s))
