def decimal_a_binario(decimal):
    binario = 0
    i = 0 # i es contador de posicion para ser usado como exponente de la base
    while decimal > 0:
        digito  = decimal%2
        decimal = decimal//2
        binario = binario+digito*(10**i)
        i = i+1
    return binario

def binario_a_decimal(bin):
    decimal = 0
    for i in range (0,len(bin),1): # esta estructura repetitiva empezara desde 0 y aumentara en 1 hasta el ultimo caracter del número binario.
        bina = int(bin[i]) # "bina" obtendra la lista de caracteres del número binario empezando por el primero hasta llegar al ultimo y los pasara a entero.
        # bina" sera multiplicado por 2 elevado por el número de la longitud del digito menos 1 y menos el valor de la variable itinerante
        # decimal" acumulara el valor en cada repetición
        decimal = decimal + bina*(2**(len(bin)-1-i))
    return decimal

def ingresar_b():
    # Funcion para validar si el numero ingresado es binario
    a = input("Ingrese el numero binario a convertir en decimal: ")
    if a == "" :
        print("No ingreso ningun dato, intentelo otra vez.")
        return ingresar_b()
    for i, x in enumerate(a):
        if x not in "01":
            print("El dato ingresado no es un numero binario, intentelo otra vez.")
            return ingresar_b()
            break
    return a

def ingresar_d():
    # Funcion para validar si el numero ingresado es decimal
    a = input("Ingrese el numero decimal a convertir en binario: ")
    if a == "" :
        print("No ingreso ningun dato, intentelo otra vez.")
        return ingresar_d()
    for i, x in enumerate(a):
        if x not in "0123456789":
            print("El dato ingresado no es un numero decimal, intentelo otra vez.")
            return ingresar_d()
            break
    return int(a)


#---------------------------------------------------
# Main
while True :
    print("Convertir:\n1-Binario a decimal.\n2-Decimal a binario.\n3-Salir.")
    opcion = int(input("Ingrese que funcion desea utilizar: "))
    if opcion == 1 :
        print("El numero ingresado en decimal es: ",binario_a_decimal(ingresar_b()))
    elif opcion == 2 :
        print("El numero ingresado en binario es: ",decimal_a_binario(ingresar_d()))
    elif opcion == 3 :
        break
    else :
        print("Opcion invalida, intente de nuevo.")

#---------------------------------------------------