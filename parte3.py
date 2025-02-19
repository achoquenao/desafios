import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Parâmetros da função de consumo escolhida
alpha = 1.0  # ajuste conforme necessário
beta = 0.5   # ajuste conforme necessário
gamma = 0.2  # ajuste conforme necessário

# Defina aqui a função de consumo que você está analisando
def consumo_energia(r):
    # Troque a função de acordo com a escolha atual
    return alpha / r + beta * r  # Exemplo: Função Inversa

# Derivada primeira da função de consumo (modifique de acordo com a função escolhida)
def derivada_primeira(r):
    return -alpha / r**2 + beta

# Derivada segunda da função de consumo (modifique de acordo com a função escolhida)
def derivada_segunda(r):
    return 2 * alpha / r**3

# Encontrar ponto de mínimo local
resultado = minimize(consumo_energia, x0=1.0, bounds=[(0.1, None)])
r_otimo = resultado.x[0]

# Valores para o eixo x
r_values = np.linspace(0.1, 5, 500)

# Cálculo dos valores de f(r), f'(r) e f''(r)
f_values = consumo_energia(r_values)
f_prime_values = derivada_primeira(r_values)
f_double_prime_values = derivada_segunda(r_values)

# Plotagem dos gráficos
plt.figure(figsize=(14, 8))

# Gráfico de f(r)
plt.subplot(3, 1, 1)
plt.plot(r_values, f_values, label=r"$f(r)$")
plt.axvline(r_otimo, color='r', linestyle="--", label=f"Min. em r = {r_otimo:.2f}")
plt.title("Função de Consumo de Energia")
plt.xlabel("Taxa de Atualização (r)")
plt.ylabel("f(r)")
plt.legend()

# Gráfico de f'(r)
plt.subplot(3, 1, 2)
plt.plot(r_values, f_prime_values, label=r"$f'(r)$", color="purple")
plt.axhline(0, color='black', linestyle="--")
plt.title("Derivada Primeira de f(r)")
plt.xlabel("Taxa de Atualização (r)")
plt.ylabel("f'(r)")
plt.legend()

# Gráfico de f''(r)
plt.subplot(3, 1, 3)
plt.plot(r_values, f_double_prime_values, label=r"$f''(r)$", color="green")
plt.axhline(0, color='black', linestyle="--")
plt.title("Derivada Segunda de f(r)")
plt.xlabel("Taxa de Atualização (r)")
plt.ylabel("f''(r)")
plt.legend()

plt.tight_layout()
plt.show()

# Exibindo os resultados
print(f"O valor ótimo de r que minimiza o consumo de energia é aproximadamente: {r_otimo:.4f} segundos")
print(f"Consumo de energia mínimo: {consumo_energia(r_otimo):.4f}")
