n = int(input('Digite um número: '))
print('O dobro de \033[1;33m{}\033[m é \033[1;33m{}\033[m, o triplo é \033[1;33m{}\033[m e a raiz quadrada é \033[1;33m{:.2f}\033[m'.format(n, n * 2, n * 3, n ** (1/2)))
