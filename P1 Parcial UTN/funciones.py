
def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Cargar nombres de participantes")
    print("2. Cargar puntuaciones de los jurados")
    print("3. Mostrar puntuaciones y promedios")
    print("4. Participantes con promedio mayor a 4")
    print("5. Participantes con promedio mayor a 7")
    print("6. Promedio de cada jurado")
    print("7. Jurado más estricto")
    print("8. Buscar participante por nombre")
    print("9. Top 3 participantes (mayor puntaje promedio)")
    print("10. Participantes ordenados alfabéticamente")
    print("0. Salir")

def crear_array(tamaño: int, valor_inicial: int = 0) -> list:
    lista = []
    for i in range(tamaño):
        lista += [valor_inicial]
    return lista

def calcular_promedio(lista: list) -> float:
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    promedio = total / len(lista)
    return promedio



def validar_str(palabra:str) -> bool:
    if len(palabra) < 3:
        return False
    
    for letras in palabra:
        codigo = ord(letras)
        if not ((65 <= codigo <= 90) or (97 <= codigo <= 122) or codigo == 32 or codigo == 164 or codigo == 165):
            return False
    return True


def validar_numeros(str:str) -> bool:
    for numeros in str:
        codigo = ord(numeros)
        if not (48 <= codigo <= 57):
            return False
        return True


def cargar_nombres(array:list) -> list:
    for i in range(len(array)):
        while True:
            str_nuevo = input(f"Agrege el nombre del {i+1} concursante: ")
            if validar_str(str_nuevo):
                array[i] = str_nuevo
                print("Cargado con exito!")
                break
            else:
                print("Error! Intentelo de nuevo")

def cargar_puntuaciones(nombres:list, puntuaciones1:list, puntuaciones2:list, puntuaciones3:list) -> None:
    for i in range(len(puntuaciones1)):
            print(f"Cargando puntajes del concursante:{nombres[i]}")
            while True:
                nueva_puntuaciones = input(f"Nota del jurado 1: ")
                if validar_numeros(nueva_puntuaciones):
                    nueva_puntuaciones = int(nueva_puntuaciones)
                    if (0 <= nueva_puntuaciones <= 10):
                        puntuaciones1[i] = nueva_puntuaciones
                        break
                    else:
                        print("El numero tiene que ser del 0-10")
                else: 
                    print("Error intentelo de nuevo ")
            
            while True:
                nueva_puntuaciones = input(f"Nota del jurado 2: ")
                if validar_numeros(nueva_puntuaciones):
                    nueva_puntuaciones = int(nueva_puntuaciones)
                    if (0 <= nueva_puntuaciones <= 10):
                        puntuaciones2[i] = nueva_puntuaciones
                        break
                    else:
                        print("El numero tiene que ser del 0-10")
                else: 
                    print("Error intentelo de nuevo ")

            while True:
                nueva_puntuaciones = input(f"Nota del jurado 3: ")
                if validar_numeros(nueva_puntuaciones):
                    nueva_puntuaciones = int(nueva_puntuaciones)
                    if (0 <= nueva_puntuaciones <= 10):
                        puntuaciones3[i] = nueva_puntuaciones
                        break
                    else:
                        print("El numero tiene que ser del 0-10")
                else: 
                    print("Error intentelo de nuevo ")
    print("Cargado con exito!")
    return True

    
#3
def cargar_info(nombres:list, p1:list, p2:list, p3:list) -> None:
    for i in range(len(nombres)):
        print(f"Estos son los datos del concursante: {nombres[i]}")
        print(f"Jurado 1: {p1[i]}")
        print(f"Jurado 2: {p2[i]}")
        print(f"Jurado 3: {p3[i]}")
        print(f"Con promedio: {(p1[i] + p2[i] + p3[i]) / 3} / 10")
    print("Cargadas con exito!")
    
    return True

#4
def promedio_mayor_a_4(nombres:list, p1:list, p2:list, p3:list) -> None:
    for i in range(len(nombres)):
        promedio = (p1[i] + p2[i] + p3[i]) /3
        if promedio >= 4:
            print(f"El concursante {nombres[i]} Tiene el promedio mayor a 4 con {promedio}")
            
        
#5
def promedio_mayor_a_7(nombres:list, p1:list, p2:list, p3:list) -> None:
    for i in range(len(nombres)):
        promedio = ((p1[i] + p2[i] + p3[i]) /3)
        if promedio >= 7:
            print(f"El concursante {nombres[i]} Tiene el promedio mayor a 7 con {promedio}")   


def promedio_Juecez(p1:list, p2:list, p3:list):
    print(f"El promedio del juez 1 es: {calcular_promedio(p1)}")
    print(f"El promedio del juez 2 es: {calcular_promedio(p2)}")
    print(f"El promedio del juez 3 es: {calcular_promedio(p3)}")

def juez_estricto(p1:list, p2:list, p3:list):
    promp1 = calcular_promedio(p1)
    promp2 = calcular_promedio(p2)
    promp3 = calcular_promedio(p3)

    menor = promp1
    if promp2 < menor:
        menor = promp2
    elif promp3 < menor:
        menor = promp3
    mensaje = "El juez más estricto es: "

    hay_varios = False
    primero = True

    if promp1 == menor:
        if not primero:
            mensaje += " - "
            hay_varios = True
        mensaje += "Juez 1 "
        
    if promp2 == menor:
        if not primero:
            mensaje += " - "
            hay_varios = True
        mensaje += "Juez 2 "
    
    if promp3 == menor:
        if not primero:
            mensaje += " - "
            hay_varios = True
        mensaje += "Juez 3 "

    if hay_varios:
        mensaje += print("Empate!!")

    print(f"{mensaje}, Con el promedio {menor}")
    return True

def encontrar_nombre(nombres: list, p1: list, p2: list, p3: list) -> bool:
    print(f"(mini ayuda = {nombres})")
    buscar_nombre = input("¿Qué nombre desea encontrar? ").lower()

    encontrado = False

    for i in range(len(nombres)):
        if nombres[i].lower() == buscar_nombre:
            print("--- Nombre encontrado----")
            print(f"Nombre: {nombres[i]}")
            print(f"Jurado 1: {p1[i]}")
            print(f"Jurado 2: {p2[i]}")
            print(f"Jurado 3: {p3[i]}")
            encontrado = True

    if not encontrado:
        print(" No se ha encontrado ningún participante con ese nombre.")

    return encontrado

def top_3(nombres: list, p1: list, p2: list, p3: list) -> None:
    promedios = [0] * len(nombres)
    for i in range(len(nombres)):
        promedios[i] = (p1[i] + p2[i] + p3[i]) / 3
    
    for i in range(len(promedios) - 1):
        for j in range(i + 1, len(promedios)):
            if promedios[i] < promedios[j]:
                auxiliar = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = auxiliar

                axuliar = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = axuliar

                aux = p1[i]
                p1[i] = p1[j]
                p1[j] = aux

                aux = p2[i]
                p2[i] = p2[j]
                p2[j] = aux

                aux = p3[i]
                p3[i] = p3[j]
                p3[j] = aux
    print(f"Aqui tienes el top 3:")
    for i in range(0, 3):
        promedio = (p1[i] + p2[i] + p3[i]) / 3
        print(f"El {i+1} concursante: {nombres[i]} con el promedio: {promedio}")

def ordenar_por_nombre(nombres: list, p1: list, p2: list, p3: list) -> None:
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            if nombres[i].lower() > nombres[j].lower():
                auxiliar = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = auxiliar

                aux = p1[i]
                p1[i] = p1[j]
                p1[j] = aux

                aux = p2[i]
                p2[i] = p2[j]
                p2[j] = aux

                aux = p3[i]
                p3[i] = p3[j]
                p3[j] = aux

    for i in range(len(nombres)):
        promedio = (p1[i] + p2[i] + p3[i]) / 3
        print(f"Nombre del concursante: {nombres[i]}")
        print(f"Puntajes que obtuvo del juez 1: {p1[i]}")
        print(f"Juez 2: {p2[i]}")
        print(f"Juez 3: {p3[i]}")
        print(f"Con un promedio de: {promedio}")