def custom_max(n1: int, n2: int):
    """Al darme dos numeros de entrada regresare el maximo de ambos

    Args:
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar

    Returns:
        int : Mayor de ambos
    """
    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    else:
        raise Exception("Los valores no pueden ser")
    
n1 = input("Dame el primer numero: ")
n2 = input("Dame el segundo numero: ")

print(custom_max(n1,n2))