import numpy as np
from scipy.optimize import minimize

# Definição dos parâmetros (valores hipotéticos de alpha e beta)
alpha = 1.0  # impacto do consumo com maior frequência de GPS
beta = 0.5   # impacto do aumento no tempo entre atualizações

# Função de consumo de energia
def consumo_energia(r):
    return alpha / r + beta * r

# Derivada da função de consumo de energia
def derivada_consumo_energia(r):
    return -alpha / (r ** 2) + beta

# Função para encontrar o valor ótimo de r
def otimizar_taxa_atualizacao():
    # Estabelece um valor inicial para r (não pode ser zero)
    r_inicial = 1.0

    # Função de minimização da energia (apenas valores positivos para r)
    resultado = minimize(consumo_energia, r_inicial, bounds=[(0.1, None)])

    # Verificação do resultado
    if resultado.success:
        r_otimo = resultado.x[0]
        print(f"O valor ideal de r que minimiza o consumo de energia é aproximadamente: {r_otimo:.4f} segundos")
        print(f"Consumo de energia mínimo: {consumo_energia(r_otimo):.4f}")
    else:
        print("O algoritmo não conseguiu encontrar uma solução ótima.")

# Execução do algoritmo de otimização
otimizar_taxa_atualizacao()
