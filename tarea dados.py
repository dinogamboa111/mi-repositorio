import random
import os
import csv
limpiar = "cls"
os.system(limpiar)
##Creo la matriz que guardara registro de las jugadas para un posterior guardado o carga en archivo csv
registrodados = [["Jugador","Tipo dado","Cantidad de dados","Resultados", "Suma Resultado"]]
##Al tener mas de un resultado si se tira mas de un dado, lo guardamos en una matriz que estara integrada en la principal.
resultados= []  
##Definimos la tirada de los dados.
def tirar_dado4():
    return random.randint(1, 4)
def tirar_dado6():
    return random.randint(1, 6)
def tirar_dado10():
    return random.randint(1, 10)
def tirar_dado20():
    return random.randint(1, 20)

def cantidades():
    for i in range(cantidaddados):
            resultadodado = tirar_dado4()
            resultados.append(resultadodado)
            suma += resultadodado 
##defino variable para mi segundo while
sigo = True
##creo menu de seleccion.
def menu():
    print("-"*45,"\nSeleccione segun su agrado:\n1. Nuevo jugador\n2. Imprime jugadas hasta el momento.\n3. Salir del juego.\n","-"*45)

print("Bienvenido a su aplicacion favorita de dados.\n"+ "-"*45 )

while True:
    ##Pedimos nombre de jugador
    usuario = str(input("Indique el nombre del jugador que lanzara esta ronda de dados: "))
   ##Generamos un try para que el dato tomado sea siempre numero entero.
    try:
        tipodado = int(input("Ingrese el tipo de dado que desea lanzar( puede ser de 4, 6, 10 o 20): "))
        print(f"Selecciono el dado de {tipodado} caras.")
        cantidaddados=int(input("Indique la cantidad de dados: "))
        print(f"Selecciono {cantidaddados} dados para tirar.")
    except ValueError:
        print("El valor debe ser numerico( 4, 6, 10 o 20)")
        continue
    suma = 0
    if tipodado == 4:
        ## como tendremos aveces mas de un dado como tirada, creamos un for para recorrer esos dados.
        ## y esto lo agregamos a una matriz llamada resultados, la cual trabajara con resultado del dado
        ## y se ira sumando a la variable suma de manera automatica, para luego mostrar el resultado final.
        cantidades() 
        print(f"Resultado de los {cantidaddados} dados de {tipodado} es: {resultados} y la suma es: {suma}")
        registrodados.append((usuario, tipodado, cantidaddados, resultados, suma))
        ##con todos mis datos tomados, los guardo en mi archivo csv, para mantener registro de mis jugadas.
        with open('registrodados.csv', 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(registrodados)  
    elif tipodado == 6:
        for i in range(cantidaddados):
            resultadodado = tirar_dado6()
            resultados.append(resultadodado)
            suma += resultadodado 
        print(f"Resultado de los {cantidaddados} dados de {tipodado} es: {resultados} y la suma es: {suma}")
        registrodados.append((usuario, tipodado, cantidaddados, resultados, suma))
        with open('registrodados.csv', 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(registrodados) 
    elif tipodado == 10:
        for i in range(cantidaddados):
            resultadodado = tirar_dado10()
            resultados.append(resultadodado)
            suma += resultadodado 
        print(f"Resultado de los {cantidaddados} dados de {tipodado} es: {resultados} y la suma es: {suma}")
        registrodados.append((usuario, tipodado, cantidaddados, resultados, suma))
        with open('registrodados.csv', 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(registrodados) 
    elif tipodado == 20:
        for i in range(cantidaddados):
            resultadodado = tirar_dado20()
            resultados.append(resultadodado)
            suma += resultadodado 
        print(f"Resultado de los {cantidaddados} dados de {tipodado} es: {resultados} y la suma es: {suma}")
        registrodados.append((usuario, tipodado, cantidaddados, resultados, suma))
        with open('registrodados.csv', 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(registrodados) 
    else:
        print("El valor debe ser numerico( 4, 6, 10 o 20)")
        continue
    while sigo:
        menu()
        try:   
            eleccion=int(input("Ingrese su seleccion: "))
        except ValueError:
            print("Digite una opcion entre 1 y 3.")
            continue
        if eleccion == 1:
            usuario=""
            tipodado=0
            cantidaddados=0
            suma=0
            del resultados[:]
            break
        elif eleccion == 2:
            with open ('registrodados.csv', 'r', newline='') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                for fila in lector_csv:
                    print(fila)
            usuario=""
            tipodado=0
            cantidaddados=0
            suma=0
            del resultados[:]
            continue
        elif eleccion == 3:
            print("Gracias por usar nuestro programa.")
            quit()
        else:
            print("Digite una opcion entre 1 y 3.")
            continue
    



    
    
