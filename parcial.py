import re
import json

def menu_principal()->None:
    '''
    Funcion: Esta funcion espera el numero ingresado para luego entrar en el caso de la opcion elegida. 
    Parametros: No recibe ningun parametro.
    Retorna: No retorna nada.
    '''
    lista_jugadores = leer_json("C:\\Users\\User\\Desktop\\Cursada Python\\Parcial\\dt.json")
    numero_ingresado = None
    acceder_opcion = False
    promedio_de_puntos = None
    lista_aux = lista_jugadores[:]
    while True:
        match validar_opciones_de_menu():
            case '1':
                imprimir_jugadores(lista_jugadores, "posicion")
            case '2':
                mostar_indice_jugadores(lista_jugadores, "nombre")
                numero_ingresado = comprobar_indice(lista_jugadores)
                if(numero_ingresado != -1):
                    mostrar_estadisticas_jugador(lista_jugadores, numero_ingresado, "estadisticas")
                    acceder_opcion = True
            case '3':
                if(acceder_opcion == True):
                    crear_csv_jugador_especifico(lista_jugadores, numero_ingresado, "jugador_especifico.csv")
                else:
                    print("No se puede acceder a la opcion.")
            case '4':
                if(buscar_jugador_por_nombre_y_logros(lista_jugadores) == -1):
                    print("No se encontro al jugador")
            case '5':
                promedio_de_puntos = sacar_promedio(lista_aux,"estadisticas" , "promedio_puntos_por_partido")
                print("El promedio es: {0}".format(promedio_de_puntos))
                lista_aux = ordenar_por_nombre(lista_aux, "asc", "nombre")
                if(lista_aux != -1):
                    imprimir_lista_orden(lista_aux, "estadisticas", "promedio_puntos_por_partido")
            case '6':
                if(buscar_jugador_por_nombre_y_salon_fama(lista_jugadores) == -1):
                    print("No se encontro al jugador")
            case '7':
                mostrar_jugador_mayor_cantidad(lista_aux,"des","estadisticas","rebotes_totales")
            case '8':
                mostrar_jugador_mayor_cantidad(lista_aux,"des","estadisticas","porcentaje_tiros_de_campo")
            case '9':
                mostrar_jugador_mayor_cantidad(lista_aux,"des","estadisticas","asistencias_totales")
            case '10':
                mostrar_mayores_que_valor(lista_aux, "estadisticas", "promedio_puntos_por_partido")
            case '11':
                mostrar_mayores_que_valor(lista_aux, "estadisticas", "promedio_rebotes_por_partido")
            case '12':
                mostrar_mayores_que_valor(lista_aux, "estadisticas", "promedio_asistencias_por_partido")
            case '13':
                mostrar_jugador_mayor_cantidad(lista_aux,"des","estadisticas","robos_totales")
            case '14':
                mostrar_jugador_mayor_cantidad(lista_aux,"des","estadisticas","bloqueos_totales")
            case '15':
                mostrar_mayores_que_valor(lista_aux, "estadisticas", "porcentaje_tiros_libres")
            case '16':
                calcular_puntos_por_partidos(lista_aux, "des", "estadisticas", "promedio_puntos_por_partido")
            case '17':
                buscar_jugador_mas_logros(lista_aux, "logros")
            case '18':
                mostrar_mayores_que_valor(lista_aux, "estadisticas", "porcentaje_tiros_triples")
            case '19':
                buscar_jugador_mas_temporadas(lista_aux, "estadisticas", "temporadas")
            case '20':
                ordenar_jugadores_por_posicion(lista_aux, "posicion", "estadisticas", "porcentaje_tiros_de_campo")
            case '21':
                crear_csv_jugadores_ranking("ranking_jugadores.csv", lista_aux)
            case '22':
                contar_por_tipo_posicion(lista_aux)
            case '23':
                mostar_lista_All_Star(lista_aux)
            case '24':
                mostrar_mejores_estadisticas(lista_aux)
            case '25':
                comparar_estadisticas(lista_aux)
            case '0':
                print("Hasta Luego!!")
                break
            case '-1':
                print("Error, reingrese nuevamente!")
        
def validar_opciones_de_menu()->str:
    '''
    Funcion: La funcion se encarga de de imprimir el menu y analizar si los numeros ingresados corresponden a opciones validas para el menu.
    Parametros: No recibe ningun parametro.
    Retorna: Retorna la opcion que cumple con el requerimiento del menu y en caso de que no devuelve un "-1".
    '''
    print("\nMenu Principal\n1. Mostrar la lista de todos los jugadores del Dream Team.\n2. Seleccionar un jugador por su índice.\n3. Guardar estadísticas del punto anterior en un archivo CSV.\n4. Buscar un jugador por su nombre y mostrar sus logros.\n5. Calcular el promedio de puntos, ordenado por nombre de manera ascendente.\n6. Ingresar un jugador y saber si es miembro del Salón de la Fama.\n7. Calcular el jugador con la mayor cantidad de rebotes totales.\n8. Calcular el jugador con el mayor porcentaje de tiros de campo.\n9. Calcular el jugador con la mayor cantidad de asistencias totales.\n10. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido\n11. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\n12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.\n13. Calcular el jugador con la mayor cantidad de robos totales.\n14. Calcular el jugador con la mayor cantidad de bloqueos totales.\n15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior\n16. Calcular el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\n17. Calcular el jugador con la mayor cantidad de logros obtenidos.\n18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior.\n19. Calcular el jugador con la mayor cantidad de temporadas jugadas.\n20. Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior.\n21. BONUS\n22. La cantidad de jugadores que hay por cada posición\n23. Lista de los jugadores All_Star.\n24. Cual es el mejor jugador en cada estadistica.\n25. El jugador que tiene la mejores estadisticas.\n0. Salir.")
    opcion = input("Ingrese una opcion: ")
    analizar = re.match("^([0-9]|1[0-9]|2[0-5])$",opcion)
    if(analizar != None):
        return opcion
    else:
        return '-1'  
    
def leer_json(nombre_archivo:str):
    '''
    Funcion: Funcion que sirve para leer archivo JSON y guardar en una lista.
    Parametros:
    -nombre_archivo(str): El nombre del archivo con el cual se busca.
    Retorno: Retorna una lista con los diccionarios extraidos del archivo json, ecaso de error retorna -1.
    '''
    lista = []
    retorno = -1
    if(nombre_archivo == None):
        return retorno
    else:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            dict = json.load(archivo)
            lista = dict["jugadores"]
        return lista

#------------------------------------------------------- Punto 1
def imprimir_jugadores(lista:list, key:str)->int:
    '''
    Funcion: La funcion se encarga de mostrar todos los nombres de la lista con el valor de la key pasada por parametro.
    Parametros: 
    -lista(list): Una lista de diccionarios, en la cual cada diccionario representa un elemento con claves y valores.
    Retorno: En caso de que haya error retorna -1, en caso de que no, se encarga solamente de imprimir.
    '''
    retorno = -1
    if(len == [] or key == None):
        return retorno
    else:
        for jugador in lista:
            print("{0} - {1}".format(jugador["nombre"], jugador[key]))

#------------------------------------------------------- Punto 2
def mostar_indice_jugadores(lista:list, key:str)->int:
    '''
    Funcion: La funcion se encarga de mostrar cada jugador con su indice en la lista.
    Parametros: 
    -lista(list): Una lista que tiene diccionarios dentro.
    -key(str): Clave que nos permite acceder al valor.
    Retorno: Retorna -1 en caso de que no funcionen los parametros.
    '''
    retorno = -1
    if(lista == [] or key == None):
        return retorno
    else:
        for indice in range(len(lista)):
            print("{0}. {1}".format(indice+1, lista[indice][key]))

def comprobar_indice(lista:list)->int:
    '''
    Funcion: Comprueba si el indice ingresado por el usuario es el correcto dentro de los parametros de la lista.
    Parametro: 
    -lista(list): Una lista de diccionarios donde cada uno sera un indice.
    Retorno: En caso de que todo funcione retornara el numero ingresado, en caso de que no retornara -1.
    '''
    retorno = -1
    numero = None
    if(lista == []):
        return retorno
    else:
        numero = input("Ingrese un numero (1-{0}): ".format(len(lista)))
        numero = int(numero)
        while(numero < 1 or numero > len(lista)):
            numero = input("Error, reingrese numero (1-{0}): ".format(len(lista)))
            numero = int(numero)
        return numero

def mostrar_estadisticas_jugador(lista:list, num:int, key:str)->int:
    '''
    Funcion: Esta funcion se encarga de mostrar el indice de el jugador y a continuacion sus estadisticas. 
    Parametro:
    -lista(list): Una lista de diccionarios donde cada uno sera un indice.
    -num(int): El indice del jugador ingresado por el usuario.
    -key(str): 
    Retorno: En caso de que no funcione retorna -1.
    '''
    retorno = -1
    if(lista == [] or num == None or key == None):
        return retorno
    else:
        print("{0}. {1}".format(num, lista[num-1]["nombre"]))
        for valor in lista[num-1][key].keys():
            print("{0} : {1}".format(valor, lista[num-1][key][valor]))

#------------------------------------------------------- Punto 3
def crear_csv_jugador_especifico(lista:list, num:int, nombre_archivo:str):
    '''
    Funcion: La funcion se escarga de crear un archivo csv de un jugador seleccionado en el punto 2. 
    Parametro:
    lista(list): Una lista de diccionarios.
    num(int): Numero de indice de el jugador seleccionado.
    nombre_archivo(str): Nombre de archivo con el cual se quiere crear.
    Retorno: En caso de que no funcione retorna -1.
    '''
    retorno = -1
    jugador = lista[num - 1]
    lista_claves = []
    lista_valor =[]
    if(lista == [] or num == None or nombre_archivo == None):
        return retorno
    else:
        #--------------------------------------cabecera
        lista_claves = list(jugador.keys())
        lista_claves = lista_claves[:2]
        lista_claves[0] = lista_claves[0].capitalize()
        lista_claves[1] = lista_claves[1].capitalize()
        for clave in jugador["estadisticas"].keys():
            lista_claves.append(clave.replace("_", " ").title())
        cabecera = ",".join(lista_claves)
        #--------------------------------------cuerpo
        lista_valor = list(jugador.values())
        lista_valor = lista_valor[:2]

        with open(nombre_archivo, "w+") as archivo:
            archivo.write(cabecera + "\n")
            for valor in jugador["estadisticas"].values():
                if isinstance(valor, (int, float)):
                    lista_valor.append(str(valor))
                else:
                    lista_valor.append(str(valor))
            dato = ",".join(lista_valor) + "\n"
            archivo.write(dato)
            print("Se imprimio el jugador {0} en {1}".format(jugador["nombre"] , nombre_archivo))
            
#------------------------------------------------------- Punto 4
def buscar_jugador_por_nombre_y_logros(lista:list)->int:
    '''
    Funcion: Funcion que sirve para analizar que el usuario ingrese por los menos tres caracteres y despues evaluar si lo ingresado se encuentra dentro de los nombres de los jugadores de cada diccionario. Si encuentra algo parecido lo guarda en una lista nueva, par luego imprimir sus resultados.
    Parametro:
    -lista(list): Una lista con diccionarios dentro.
    Retorno: Retorna menos -1 en caso de error.
    '''
    retorno = -1
    if(lista == []):
        return retorno
    else:
        nombre_ingresado = input("Ingrese nombre: ")
        analizar = re.search("[a-zA-Z]{3}", nombre_ingresado)
        jugadores_coincidentes = [] 
        if(analizar != None):
            for jugador in lista:
                if(nombre_ingresado.lower() in jugador["nombre"].lower()):
                    jugadores_coincidentes.append(jugador)
            if(jugadores_coincidentes):
                for deportista in jugadores_coincidentes:
                    print("---{0}---".format(deportista["nombre"]))
                    for key in deportista["logros"]:
                        print("{0}".format(key))
            else:
                return retorno
        else:
                return retorno
           
#------------------------------------------------------- Punto 5
def sacar_promedio(lista:list, key:str, clave:str)->float:
    '''
    Funcion: Esta funcion se encarga de sacar el promedio de las keys pasada por parametro.
    Parametros: 
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -key(str): La clave que nos permite acceder a diccionarios.
    -clave(str): Clave que nos permite traer el valor requerido.
    Retorna: Retorna el promedio de la lista ingresada por parametro, en caso de error -1.
    '''
    retorno = -1
    acumulador = 0
    contador = 0  
    promedio = 0
    
    if(lista == [] or key == None or clave == None):
        return retorno
    else:
        for jugador in lista:
            if key in jugador:
                acumulador += jugador[key][clave]
                contador += 1
        if(contador > 0):
            promedio = acumulador / contador
        return promedio

def ordenar_por_nombre(lista:list, orden:str, key:str)->list:
    '''
    Funcion: Esta funcion se encarga de ordenar la lista recibida tanto de manera ascendente como de manera descendente y segun la clave a ordenar
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -orden(str): Parametro que nos sirve para saber en que forma (ascendente/descendente) sera guardada la lista.
    -key(str): Nos indica por que clave sera la parte a ordenar.
    Retorna: Retorna la lista con los elementos cambiados segun el orden, en caso de error retorna -1.
    '''
    retorno = -1
    if(lista == [] or orden == None or key == None):
        return retorno
    else:
        flag_swap = True
        rango_lista = len(lista)
        while(flag_swap):
            flag_swap = False
            rango_lista = rango_lista-1
            for jugador in range(rango_lista):
                if((lista[jugador][key] < lista[jugador+1][key] and orden == "asc") or (lista[jugador][key] < lista[jugador+1][key] and orden == "des")):
                    aux = lista[jugador]
                    lista[jugador] = lista[jugador+1]
                    lista[jugador+1] = aux
                    flag_swap = True
        return lista

def imprimir_lista_orden(lista:list, key:str, clave:str)->int:
    '''
    Funcion: Imprime la funcion de manera ordena dependiendo de las claves que se pasen por parametro.
    Parametro: 
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -key(str): Clave que sirve para encontrar una parte de diccionario.
    -clave(str): El valor a imprimir
    Retorno: En caso de error retorna -1.
    '''
    retorno = -1
    if(lista == [] or key == None or clave == None ):
        return retorno
    else: 
        for jugador in lista:
            print("{0} - {1}:{2}".format(jugador["nombre"], clave.replace("_", " ").capitalize(), jugador[key][clave]))


#------------------------------------------------------- Punto 6
def buscar_jugador_por_nombre_y_salon_fama(lista:list)->int:
    '''
    Funcion: Buscar el nombre de un jugador segun lo ingresado por el usuario, en caso de encontrarlo imprime su nombre y si es salon de la fama.
    Parametro:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    Retorno: En caso de error retorna -1.
    '''
    retorno = -1
    if(lista == []):
        return retorno
    else:
        nombre_ingresado = input("Ingrese nombre: ")
        analizar = re.search("[a-zA-Z]{3}", nombre_ingresado)
        jugadores_coincidentes = [] 
        if(analizar != None):
            for jugador in lista:
                if(nombre_ingresado.lower() in jugador["nombre"].lower()):
                    jugadores_coincidentes.append(jugador)
            if(jugadores_coincidentes):
                for deportista in jugadores_coincidentes:
                    for logro in deportista["logros"]:
                        if(logro == "Miembro del Salon de la Fama del Baloncesto"):
                            print("---{0}---".format(deportista["nombre"]))
                            print("{0}".format(logro))
            else:
                return retorno
        else:
                return retorno

#------------------------------------------------------- Punto 7,8,9,13,14
def ordenar_por_x(lista:list, orden:str, key:str, clave:str)->list:
    '''
    Funcion: Esta funcion se encarga de ordenar la lista recibida tanto de manera ascendente como de manera descendente y las claves de los valores a ordenar.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -orden(str): Parametro que nos sirve para saber en que forma (ascendente/descendente) sera guardada la lista.
    -key(str): Nos indica por que clave sera la parte a ordenar.
    -clave(str):  Nos indica el valor por el cual ordenar.
    Retorna: Retorna la lista con los elementos cambiados segun el orden, en caso de error retorna -1.
    '''
    retorno = -1
    if(lista == [] or orden == None or key == None or clave == None ):
        return retorno
    else:
        flag_swap = True
        rango_lista = len(lista)
        while(flag_swap):
            flag_swap = False
            rango_lista = rango_lista-1
            for jugador in range(rango_lista):
                if((lista[jugador][key][clave] > lista[jugador+1][key][clave] and orden == "asc") or (lista[jugador][key][clave] < lista[jugador+1][key][clave] and orden == "des")):
                    aux = lista[jugador]
                    lista[jugador] = lista[jugador+1]
                    lista[jugador+1] = aux
                    flag_swap = True
        return lista
    

def imprimir_un_jugador(lista:list, indice:int, key:str, clave:str)->None:
    '''
    Funcion: Imprime un jugador dependiendo de el indice que se pase por parametro.
    Parametro:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -indice(int): Indice del jugador a imprimir.
    -key(str): Clave del jugador para acceder.
    -clave(str): Clave que nos permite el valor.
    Retorno: EN caso de error retorna -1.
    '''
    retorno = -1
    if(lista == [] or indice == None or key == None or clave == None):
        return retorno
    else: 
        print("{0} - {1} : {2}".format(lista[indice]["nombre"], clave.replace("_", " ").capitalize(), lista[indice][key][clave]))

def mostrar_jugador_mayor_cantidad(lista:list, orden:str, key:str, clave:str)->int:
    '''
    Funcion: Muestra el elemento de una lista con mayor cantidad de un valor especificado, utilizando la función imprimir_un_jugador.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -orden(str): Parametro que nos sirve para saber en que forma (ascendente/descendente) sera guardada la lista.
    -key(str): Nos indica por que clave sera la parte a ordenar.
    -clave(str):  Nos indica el valor por el cual ordenar.
    Retorno:En caso de error, retorna -1.
    '''
    retorno = -1
    indice = 0
    if(lista == [] or orden == None or key == None or clave == None ):
        return retorno
    else:
        nueva_lista = ordenar_por_x(lista, orden, key, clave)
        if(nueva_lista != -1):
            imprimir_un_jugador(nueva_lista, indice, key, clave)
        else:
            print("No se puede realizar calculo.")

#------------------------------------------------------- Punto 10,11,12,15,18
def sacar_maximo(lista:list,key:str, clave:str):
    '''
    Funcion: Funcion que se encarga de sacar el numero maximo de la lista en base a la claves pasadas por parametro. 
    Parametro:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -key(str): Clave de jugador para acceder.
    -clave(str): Clave que nos permite acceder al valor.
    Retorno: En caso de error retorna -1.
    '''
    maximo = 0
    retorno = -1
    if(lista == [] or key == None or clave == None):
        return retorno
    else:
        for jugador in lista:
            if(jugador[key][clave] > maximo):
                maximo = jugador[key][clave]
        return maximo 

def sacar_minimo(lista:list,key:str, clave:str):
    '''
    Funcion: Funcion que se encarga de sacar el numero minimo de la lista en base a la claves pasadas por parametro.
    Parametro:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -key(str): Clave de jugador para acceder.
    -clave(str): Clave que nos permite acceder al valor.
    Retorno: En caso de error retorna -1.
    '''
    minimo = sacar_maximo(lista, key, clave)
    retorno = -1
    if(lista == [] or key == None or clave == None):
        return retorno
    else:
        for jugador in lista:
            if(jugador[key][clave] < minimo):
                minimo = jugador[key][clave]
        return minimo 

def ingresar_valor(lista:list,key:str, clave:str)->float:
    '''
    Funcion: Esta funcion se encarga de evaluar si el numero ingresado entra en los parametros de minimo y maximo, en caso de que no, se debera ingresar numero hasta que se cumpla el proposito.
    Parametro:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -key(str): Clave de jugador para acceder.
    -clave(str): Clave que nos permite acceder al valor.
    Retorno: Retorna el numero corecto ingresado.
    '''
    maximo = sacar_maximo(lista, key, clave)
    minimo = sacar_minimo(lista, key, clave)
    retorno = -1
    if(lista == [] or key == None or clave == None):
        return retorno
    else:
        numero = input("Ingrese valor({0}-{1}): ".format(minimo, maximo))
        validar = re.search(r"[0-9]+(\.[0-9]+)?$", numero)
        if(validar != None):
            numero = float(numero)
            if(numero <=  maximo and numero >= minimo):
                return numero
            else:
                while(numero > maximo or numero < minimo):
                    numero = input("Reingrese valor({0}-{1}): ".format(minimo, maximo))
                    validar = re.search(r"[0-9]+(\.[0-9]+)?$", numero)
                    if(validar != None):
                        numero = float(numero)
                        if(numero <=  maximo and numero >= minimo):
                            return numero
        else:
            return retorno

        
def obtener_mayores_a_valor_ingresado(lista:list, key:str, clave:str)->int:
    '''
    Funcion: La funcion se encarga de evaluar si los jugadores de la lista (claves) son capaz de sobrepasar el numero ingresado por el usuario y los imprime.
    Parametro:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -key(str): Clave de jugador para acceder.
    -clave(str): Clave que nos permite acceder al valor.
    Retorno: EN caso de error retorna -1.
    '''
    retorno = -1
    if(lista == [] or key == None or clave == None):
        return retorno
    else:
        numero = ingresar_valor(lista, key, clave)
        nueva_lista =[]
        if(numero != -1):
            for jugador in lista:
                if(jugador[key][clave] >= numero):
                    nueva_lista.append(jugador)
            nueva_lista = ordenar_por_x(nueva_lista, "asc", key, clave)
            return nueva_lista
        else:
            return retorno

def mostrar_mayores_que_valor(lista:list, key:str, clave:str)->int:
    '''
    Funcion: Muestra los elementos de una lista que son mayores que un valor especificado, utilizando la función imprimir_lista_orden.
    Parametros:
    - lista(list): Una lista de diccionarios donde cada elemento contiene información a ser analizada.
    - key(str): La clave utilizada para comparar los valores de los elementos de la lista.
    - clave(str): El valor de referencia utilizado para determinar si un elemento es mayor o no.
    Retorno: En caso de error, retorna -1.
    '''
    retorno = -1
    if(lista == [] or key == None or clave == None):
        return retorno
    else:
        lista_nueva = obtener_mayores_a_valor_ingresado(lista, key, clave)
        if(lista_nueva != -1):
            imprimir_lista_orden(lista_nueva, key, clave)
        else:
            print("No se puede realizar calculo.")

#------------------------------------------------------- Punto 16
def calcular_puntos_por_partidos(lista:list, orden:str, key:str, clave:str)->int:
    '''
    Funcion: Funcion que se encarga de crear una nueva lista de manera ordenada descendentemente y sacar el jugador de la ultima posicion de la lista.
    Parametro:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -key(str): Clave de jugador para acceder.
    -clave(str): Clave que nos permite acceder al valor.
    Retorno: En caso de error retorna -1.
    '''
    retorno = -1
    if(lista == [] or orden == None or key == None or clave == None):
        return retorno
    else:
        lista_nueva = []
        promedio = 0
        lista_nueva = ordenar_por_x(lista,orden,key,clave)
        lista_nueva = lista_nueva[:len(lista_nueva)-1]
        promedio = sacar_promedio(lista_nueva, key, clave)
        imprimir_lista_orden(lista_nueva, key, clave)
        print("El promedio de puntos por partido del equipo es: {0}".format(promedio))

#------------------------------------------------------- Punto 17
def buscar_jugador_mas_logros(lista:list, key:str)->int:
    '''
    Funcion: La funcion busca el jugador con mas logros conseguidos y lo imprime.
    Parametros:
    -lista(list):Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -key(str): Clave que nos permite contabilizar su valor.
    Retorno: En caso de error retorna -1.
    '''
    retorno = -1
    mayor_cantidad = 0
    numero = None
    if(lista == [] or key == None):
        return retorno
    else:
        for indice in range(len(lista)):
            if(len(lista[indice][key]) > mayor_cantidad):
                mayor_cantidad = len(lista[indice][key])
                numero = indice
        print("{0} - {1} : {2}".format(lista[numero]["nombre"], key, mayor_cantidad))

#------------------------------------------------------- Punto 19
def buscar_jugador_mas_temporadas(lista:list, key:str, clave:str)->int:
    '''
    Funcion: La funcion se encarga de evaluarlos jugadores conmas temporadas jugadas y agregarla a una nueva lista, la cual sera impresa.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -key(str): Un string que nos permite acceder a cierto campo.
    -clave(str): Una clave que nos va a a traer el valor a contabilizar.
    Retorno: En caso de error retorna -1.
    '''
    retorno = -1
    mayor_cantidad = 0
    if(lista == [] or key == None):
        return retorno
    else:
        lista_nueva = []
        for jugador in lista:
            if(jugador[key][clave] > mayor_cantidad):
                mayor_cantidad = jugador[key][clave]
        for deportista in lista:
            if(mayor_cantidad == deportista[key][clave]):
                lista_nueva.append(deportista)
        imprimir_lista_orden(lista_nueva, key, clave)
        
#------------------------------------------------------- Punto 20
def ordenar_jugadores_por_posicion(lista:list, key:str, segunda_key:str, clave:str)->list:
    '''
    Funcion: Esta funcion se encarga de ordenar por key de forma alfabetica, pero antes se encarga de que el usuario ingrese un valor. La cual va a ser la base para que los que compongan la nueva lista deberan sobrepasar la primera lista pasada por parametro.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -key(str): La clave con la cual sera analizada alfabeticamente.
    -segunda_key(str): La clave que nos permitir acceder al campo.
    -clave(str):  Clave que nos dara los valores a examinar con el valor ingresado.
    Retorna: Retorna la lista ordenada alfabeticamente, en caso de error -1.
    '''
    retorno = -1
    nueva_lista = []
    if(lista == [] or key == None):
        return retorno
    else:
        nueva_lista = obtener_mayores_a_valor_ingresado(lista, segunda_key, clave)
        flag_swap = True
        rango_lista = len(nueva_lista)
        while(flag_swap):
            flag_swap = False
            rango_lista = rango_lista-1
            for jugador in range(rango_lista):
                if(nueva_lista[jugador][key] > nueva_lista[jugador+1][key]):
                    aux = nueva_lista[jugador]
                    nueva_lista[jugador] = nueva_lista[jugador+1]
                    nueva_lista[jugador+1] = aux
                    flag_swap = True
        imprimir_jugadores(nueva_lista, "posicion")
        return nueva_lista

#------------------------------------------------------- Punto 21
def calcular_ranking_posiciones(lista:list)->list:
    '''
    Funcion:La función se encarga de calcular el ranking de posiciones para cada estadística en la lista de jugadores.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    Retorno: Retorna una lista de jugadores ordenada, en caso de error, retorna -1.
    '''
    retorno = -1
    if(lista == []):
        return retorno
    else:
        lista_estaditicas = ["puntos_totales", "rebotes_totales", "asistencias_totales", "robos_totales"]
        for estadistica in lista_estaditicas:
            lista_odenada = ordenar_por_x(lista,"des","estadisticas",estadistica)
            jugadores_con_estadistica = []
            for indice in range(len(lista_odenada)):
                jugador = lista_odenada[indice]
                nombre = jugador["nombre"]
                jugador["estadisticas"][estadistica] = indice + 1
                jugador_modificado = {"nombre":nombre,"estadisticas":jugador["estadisticas"]}
                jugadores_con_estadistica.append(jugador_modificado)
        print(jugadores_con_estadistica)
        return jugadores_con_estadistica


def generar_texto_ranking(lista:list)->str:
    '''
    Funcion: La función se encarga de generar un texto con las estadísticas de los jugadores en formato CSV.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    Retorno: Retorna un texto con el ranking de jugadores, en caso de error retorna -1.
    '''
    retorno = -1
    if(lista == []):
        return retorno
    else:
        lista_ranking = calcular_ranking_posiciones(lista)
        lista_claves = ["Nombre","Puntos","Rebotes","Asistencias","Robos"]
        filas = []
        for jugador in lista_ranking:
            valores = [str(jugador["nombre"]), str(jugador["estadisticas"]["puntos_totales"]), str(jugador["estadisticas"]["rebotes_totales"]), str(jugador["estadisticas"]["asistencias_totales"]), str(jugador["estadisticas"]["robos_totales"])]
            fila = ",".join(valores)
            filas.append(fila)
        claves = ",".join(lista_claves)
        datos = "{0}\n{1}".format(claves,"\n".join(filas))
        return datos
    
def crear_csv_jugadores_ranking(nombre_archivo:str, lista:list)->int:
    '''
    Funcion: La función se encarga de crear un archivo CSV con el ranking de jugadores y sus posiciones de estadísticas.
    Parametros:
    -nombre_archivo(str): Nombre por el cual se guarda el archivo CSV.
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    Retorno: Retorna -1 en caso de error.
    '''
    retorno = -1
    if(nombre_archivo == None or lista == []):
        return retorno
    else:
        texto = generar_texto_ranking(lista)
        with open(nombre_archivo, "w+") as archivo:
            archivo.write(texto)
        print("Se creo el archivo {0}".format(nombre_archivo))



#------------------------------------------------------- Puntos extra
#------------------------------------------------------- Punto 22
def contar_por_tipo_posicion(lista:list)->dict:
    '''
    Funcion: Esta funcion permite recorrer la lista e ir contabilizando que jugador tiene algun tipo de clave (posicion) diferente. 
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    Retorno: Retorna un diccionario con la posiciones como clave y la cantidad de jugadores en ese puesto como valor, en caso de error, retorna -1.
    '''
    retorno = -1
    dic_posicion = {}
    if(lista == []):
        return retorno
    else:
        for jugador in lista:
            if(jugador["posicion"] in dic_posicion):
                dic_posicion[jugador["posicion"]] += 1
            else:
                dic_posicion[jugador["posicion"]] = 1
        for deportista, valor in dic_posicion.items():
            print("{0}:{1}".format(deportista, valor))
        return dic_posicion 


#------------------------------------------------------- Punto 23
def obtener_jugadores_All_Star(lista:list):
    '''
    Funcion: Esta funcion se encarga de crear una lista nueva con los jugadores que pertenecieron al equipo All-Star de la temporada.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    Retorno: Retorna una lista con los jugadores All-Star, en caso de error, devuelve -1.
    '''
    retorno = -1
    if(lista == []):
        return retorno 
    else:
        jugadores_all_star = []
        for jugador in lista:
            logros = jugador['logros']
            for logro in logros:
                if 'All-Star' in logro:
                    jugadores_all_star.append(jugador)
                    break
    return jugadores_all_star
        

def ordenar_por_All_Star(lista:list):
    '''
    Funcion: Ordena una lista de diccionarios según el número de veces que cada jugador ha sido seleccionado para el All-Star.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    Retorno: Una lista ordenada descendientemente según el número de selecciones al All-Star o en caso de error retorna -1.
    '''
    retorno = -1
    if(lista == []):
        return retorno 
    else:
        jugadores_All_Star = obtener_jugadores_All_Star(lista)
        jugadores = []
        for jugador in jugadores_All_Star:
            logros = jugador['logros']
            count_all_star = 0
            for logro in logros:
                matches = re.findall(r'(\d+)\s+veces\s+All-Star', logro)
                if matches:
                    count_all_star += int(matches[0])
            jugadores.append((jugador['nombre'], count_all_star))
    
        jugadores = sorted(jugadores, key=lambda x: x[1], reverse=True)
    return jugadores

def mostar_lista_All_Star(lista:list):
    '''
    Funcion: Imprime el nombre del jugador con el numero de las veces que el jugador fue All-Star.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    Retorno: Retorna -1 en caso de error.
    '''
    retorno = -1
    if(lista == []):
        return retorno 
    else:
        jugadores = ordenar_por_All_Star(lista)
        for jugador in jugadores:
            print("{0} ({1} veces All-Star)".format(jugador[0], jugador[1]))

#------------------------------------------------------- Punto 24
def obtener_mejor_jugador_por_valor(lista:list, valor:str):
    '''
    Funcion: Encuentra el mejor jugador en una lista de diccionarios según un valor específico.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    -valor(str): La clave por la cual va a ir iterando para llegar al mejor jugador en esa caracteristicas.
    Retorno: El nombre del mejor jugador y el valor máximo alcanzado en la característica especificada o en caso de error devuelve -1.
    '''
    retorno = -1
    mejor_jugador = None
    max_valor = 0
    if(lista == [] or valor == None):
        return retorno
    else:
        for jugador in lista:
            estadisticas = jugador["estadisticas"]
            if estadisticas[valor] > max_valor:
                max_valor = estadisticas[valor]
                mejor_jugador = jugador["nombre"]
    return mejor_jugador, max_valor

def mostrar_mejores_estadisticas(lista:list)->None:
    '''
    Funcion: Muestra las mejores estadísticas de los jugadores en una lista de diccionarios.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    Retorno: Retorna -1 en caso de error.
    '''
    retorno = -1
    if(lista == []):
        return retorno
    else:
        valores = {
            "temporadas": "Mayor cantidad de temporadas",
            "puntos_totales": "Mayor cantidad de puntos totales",
            "rebotes_totales": "Mayor cantidad de rebotes totales",
            "asistencias_totales": "Mayor cantidad de asistencias totales",
            "robos_totales": "Mayor cantidad de robos totales",
            "bloqueos_totales": "Mayor cantidad de bloqueos totales",
            "porcentaje_tiros_de_campo": "Mayor porcentaje de tiros de campo",
            "porcentaje_tiros_libres": "Mayor porcentaje de tiros libres",
            "porcentaje_tiros_triples": "Mayor porcentaje de tiros triples"
        }
        for valor, descripcion in valores.items():
            mejor_jugador, max_valor = obtener_mejor_jugador_por_valor(lista, valor)
            print("{0}: {1} ({2})".format(descripcion, mejor_jugador, max_valor))


#------------------------------------------------------- Punto 25
def comparar_estadisticas(lista:list)->str:
    '''
    Funcion: Esta funcion se encarga de sumar todas las estadisticas de cada jugador y comparar, para llegar al que mejor puntuacion tiene.
    Parametros:
    -lista(list): Una lista de diccionario que cada elemento tiene su clave y valor para ser analizada.
    Retorno: Retorna el nombre del jugador con mejor puntuacion, en caso de error, devuelve -1.
    '''
    retorno = -1
    mejor_jugador = None
    mejor_estadistica = 0
    if(lista == None):
        return retorno
    else:
        for jugador in lista:
            estadisticas = jugador['estadisticas']
            puntos_totales = estadisticas['puntos_totales']
            rebotes_totales = estadisticas['rebotes_totales']
            asistencias_totales = estadisticas['asistencias_totales']
            promedio_puntos_por_partido = estadisticas['promedio_puntos_por_partido']
            promedio_rebotes_por_partido = estadisticas['promedio_rebotes_por_partido']
            promedio_asistencias_por_partido = estadisticas['promedio_asistencias_por_partido']

            puntuacion = puntos_totales + rebotes_totales + asistencias_totales + promedio_puntos_por_partido + promedio_rebotes_por_partido + promedio_asistencias_por_partido

            if puntuacion > mejor_estadistica:
                mejor_estadistica = puntuacion
                mejor_jugador = jugador['nombre']

    print("El mejor jugador es {0} con {1} de puntuacion".format(mejor_jugador, mejor_estadistica))
    return mejor_jugador

menu_principal()