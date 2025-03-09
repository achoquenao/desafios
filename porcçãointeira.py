import math

# Solicita ao usuário que insira um número real
numero_real = float(input("Digite um número real: "))

# Obtém a porção inteira do número real
porcao_inteira = math.trunc(numero_real)

print(f"A porção inteira de {numero_real} é {porcao_inteira}.")
