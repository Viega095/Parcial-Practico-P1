import os
from funciones import *
nombres = crear_array(5)
puntajes_j1 = crear_array(5)
puntajes_j2 = crear_array(5)
puntajes_j3 = crear_array(5)

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            os.system("cls")
            print(">> Cargar participantes")
            cargar_nombres(nombres)
            print(f"Tienes de nombres a :{nombres}")

        elif opcion == "2":
            os.system("cls")
            print(">> Cargar puntuaciones ")
            cargar_puntuaciones(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
            
        elif opcion == "3":
            os.system("cls")
            print(">> Mostrar puntuaciones")
            cargar_info(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
            
        elif opcion == "4":
            os.system("cls")
            print(">> Participantes con promedio > 4 ")
            promedio_mayor_a_4(nombres, puntajes_j1, puntajes_j2, puntajes_j3)

        elif opcion == "5":
            os.system("cls")
            print(">> Participantes con promedio > 7 ")
            promedio_mayor_a_7(nombres, puntajes_j1, puntajes_j2, puntajes_j3)

        elif opcion == "6":
            os.system("cls")
            print(">> Promedio de cada jurado")
            promedio_Juecez(puntajes_j1, puntajes_j2, puntajes_j3)

        elif opcion == "7":
            os.system("cls")
            print(">> Jurado más estricto")
            print("-") * 50
            juez_estricto(puntajes_j1, puntajes_j2, puntajes_j3)

        elif opcion == "8":
            os.system("cls")
            print(">> Buscar participante")
            encontrar_nombre(nombres, puntajes_j1, puntajes_j2, puntajes_j3)

        elif opcion == "9":
            os.system("cls")
            print(">> Top 3 participantes")
            top_3(nombres, puntajes_j1, puntajes_j2, puntajes_j3)

        elif opcion == "10":
            os.system("cls")
            print(">> Participantes ordenados")
            ordenar_por_nombre(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
            
        elif opcion == "0":
            os.system("cls")
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

        input("Toque cualquier boton para continuar... ")
        os.system("cls")

main()
