from numeros_maximos.numero_maximo import soluciones


def max_de_tres(n1: int, n2: int, n3:int):
    """Al darme tres numeros de entrada regresare el maximo de los tres

    Args:
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar
        n3 (int): Tercer numero a comparar

    Returns:
        int : Mayor de los tres
    """
    
    n = soluciones.custom_max(n1, n2)
    n_final = soluciones.custom_max(n3, n)

    return n_final



