import os

def ejecutarScript(nombreScript):
    os.system(f"python {nombreScript}")

def ejecutarMenu():
    print("-----EJECUTAR EJERCICIOS DE CLASES-----")
    print("1.-Ejercicio1-Variables\n2.-Ejercicio2-Datos del Usuario\n3.-Ejercicio3- Operaciones suma mult\n4.-Ejercicio4-Area circulo \n5.-Ejercicio5-Rango numeros\n6.-Ejercicio6-Califiaciones\n7.-Ejercicio7-Entrada Datos\n8.-Ejercicio8-Numero para o impar\n9.- Ejerciio9-Numero Mayor que 10\n10.-Ejercicio10-Numero positivo Negativo\n11.-Ejercicio11-Adivinar un numero\n12.-Ejercicio12-Mostrar Calificacion por letra\n13.-Ejercicio13-libreria datatime\n14.-Ejercicio14-Descuento del 10%\n15.-Ejercicio15-Mejora1 Descuento\n16.-Ejercicio16-Mejora2 Descuento\n17.-Ejercio17-Tempearatura\n18.-Ejercicio18-Modelo Cognoscitivo\n19.-Ejercicio19-Agente Inteligente\n20.-Ejercicio20-papel de la Heuristica\n0.-Terminar Programa")
    
while True:
    ejecutarMenu()
    opcion=int(input("opcion a ejecutar: "))
    if opcion==1:
        ejecutarScript("Ejercicio1.py")
    elif opcion==2:
        ejecutarScript("Ejercicio2.py")
    elif opcion==3:
        ejecutarScript("Ejercicio3.py")
    elif opcion==4:
        ejecutarScript("Ejercicio4.py")
    elif opcion==5:
        ejecutarScript("Ejercicio5.py")
    elif opcion==6:
        ejecutarScript("Ejercicio6.py")
    elif opcion==7:
        ejecutarScript("Ejercicio7.py")
    elif opcion==8:
        ejecutarScript("Ejercicio8.py")
    elif opcion==9:
        ejecutarScript("Ejercicio9.py")
    elif opcion==10:
        ejecutarScript("Ejercicio11.py")
    elif opcion==11:
        ejecutarScript("Ejercicio12.py")
    elif opcion==12:
        ejecutarScript("Ejercicio14.py")
    elif opcion==13:
        ejecutarScript("libreriaDatatime.py")
    elif opcion==14:
        ejecutarScript("Ejercicio15.py")
    elif opcion==15:
        ejecutarScript("Ejercicio15Mejora1.py")
    elif opcion==16:
        ejecutarScript("Ejercicio15Mejora2.py")
    elif opcion==17:
        ejecutarScript("temperaturaCiudades.py")
    elif opcion==18:
        ejecutarScript("AgenteCognitivo.py")
    elif opcion==19:
        ejecutarScript("MultiagenteBasico.py")
    elif opcion==20:
        ejecutarScript("Heuristica.py")
    elif opcion==0:
        print("fin de programa")
        break
    else:
        print("La opcion no existe")
        break
    

