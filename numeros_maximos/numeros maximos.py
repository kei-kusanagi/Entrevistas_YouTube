from numeros_maximos.numero_maximo import soluciones
from numeros_maximos.numero_maximo_3 import solucion3numeros

seguir = True

def continuar():
    continuar = str(input("Otra operacion si o no?"))
    if continuar == "si":
        return True
    elif continuar =="no":
        print("💸Porfavor patrocinenme una computadora 😅")
        return False





while seguir:
    respuesta = int(input("cuantos numeros quieres calcular 2 o 3:"))
    if respuesta == 2:

        n1 = int(input("Dame el primer numero: "))
        n2 = int(input("Dame el segundo numero: "))
        print(soluciones.custom_max(n1, n2))
        seguir=continuar()

    else:

        n1 = int(input("Dame el primer numero: "))
        n2 = int(input("Dame el segundo numero: "))
        n3 = int(input("Dame el tercer numero: "))
        print(solucion3numeros.max_de_tres(n1, n2, n3))
        seguir=continuar()