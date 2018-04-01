num = float(input('Digite o valor em metros: '))
cm = num * 100
mm = num * 1000
print('A distancia de \033[4;33m{}m\033[m em centímetros é \033[4;33m{}cm\033[m e em milimetros é \033[4;33m{}mm\033[m'.format(num, cm, mm))
