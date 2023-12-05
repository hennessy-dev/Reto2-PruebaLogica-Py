def multiplicacion_rusa1(n1, n2):
    multiplicador = n1
    multiplicando = n2
    numeros = {}
    resultado = 0

    while multiplicador != 1:
        multiplicando = multiplicando * 2
        multiplicador = round(multiplicador/2)
        numeros[multiplicador] = multiplicando

    for clave, valor in numeros.items():
        if clave % 2 != 0:
            resultado += valor

    if n2 % 2 == 0:
        resultado += n2

    return print(resultado)

multiplicador = int(input("Ingrese el multiplicador: "))
multiplicando = int(input("Ingrese el multiplicando: "))
multiplicacion_rusa1(multiplicador, multiplicando)

