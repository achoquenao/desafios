def fibonacci(n):
    """
    Gera a sequência de Fibonacci até um número não exceder n.
    
    Args:
        n (int): Número limite para a sequência
    
    Returns:
        list: Lista contendo a sequência de Fibonacci
    
    Raises:
        ValueError: Se n for negativo
    """
    if n < 0:
        raise ValueError("O número deve ser positivo")
        
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def pertence_a_fibonacci(n):
    """
    Verifica se um número pertence à sequência de Fibonacci.
    
    Args:
        n (int): Número a ser verificado
    
    Returns:
        str: Mensagem indicando se o número pertence ou não à sequência
    """
    fib_sequence = fibonacci(n)
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

def main():
    """Função principal do programa."""
    while True:
        try:
            numero = int(input("Informe um número (ou digite um valor não numérico para sair): "))
            resultado = pertence_a_fibonacci(numero)
            print(resultado)
        except ValueError as e:
            if "deve ser positivo" in str(e):
                print("Erro: Por favor, digite um número positivo.")
            else:
                print("Programa encerrado.")
                break

if __name__ == "__main__":
    main()
