v = input("Digite algo: ")
print("Você digitou: ", v)
print("É do tipo:\033[0;33m", type(v), '\033[m')
print("É numérico:\033[0;34m", v.isnumeric(), '\033[m')
print("É alfabético:\033[0;35m", v.isalpha(), '\033[m')
print("É alfanumérico:\033[0;36m", v.isalnum(), '\033[m')
