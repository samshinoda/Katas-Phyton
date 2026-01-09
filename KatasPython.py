#1. Escribe una función que reciba una cadena de texto como parámetro y 
# devuelva un diccionario con las frecuencias 
# de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(cadena):
    frecuencias = {}
    for letra in cadena:
        if letra != " ": 
            # Uso .get(letra, 0) para obtener el valor actual o 0 si no existe,
            # simplificando el bloque if/else clásico.
            frecuencias[letra] = frecuencias.get(letra, 0) + 1    
    return frecuencias

texto = "cadena de texto"
resultado = frecuencia_letras(texto)
print(resultado)

#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
# Usa la función map()

numeros = [1, 5, 7, 8, 9]
resultado = list(map(lambda x: x * 2, numeros))
print(f"Lista original: {numeros}")
print(f"Doble de cada valor: {resultado}")

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como 
# parámetros. La función debe devolver una lista con todas las palabras de la 
# lista original que contengan la palabra objetivo.

def buscar_palabras(lista_palabras, objetivo):
    coincidencias = [] 
    for palabra in lista_palabras:
        if objetivo in palabra:
            coincidencias.append(palabra)
    return coincidencias

palabras_mar = ["mar", "marea", "submarino", "calamar", "tierra", "marte"]
objetivo = "mar"
resultado = buscar_palabras(palabras_mar, objetivo)
print(f"La palabra '{objetivo}' se encuentra en: {resultado}")

#4. Genera una función que calcule la diferencia entre los valores de dos listas. 
# Usa la función map()

def calculo_diferencia(lista1, lista2):
    resultado = map(lambda x, y: x - y, lista1, lista2)
    return list(resultado)

lista1 = [3, 5, 6, 8]
lista2 = [1, 2, 3, 9]
diferencia = calculo_diferencia(lista1, lista2)
print(f"La diferencia entre las listas es '{diferencia}'")

#5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que 
# por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media 
# es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". 
# La función debe devolver una tupla que contenga la media y el estado.

def evaluar_notas(lista_numeros, nota_aprobado=5):
    media = sum(lista_numeros) / len(lista_numeros)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)

notas_alumno = [4, 6, 5, 7, 8]
resultado = evaluar_notas(notas_alumno) 
print(f"Nota final: {resultado}")

#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n + factorial(n - 1)
    
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    resultado = map(lambda tupla: " ".join(tupla), lista_tuplas)
    return list(resultado)

nombres_completos = [("Juan", "Pérez"), ("Ana", "García"), ("Luis", "Rodríguez")]
lista_strings = tuplas_a_strings(nombres_completos)
print(lista_strings)

#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor 
# no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar 
# un mensaje indicando si la división fue exitosa o no.

def dividir_numeros():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("Error: Has introducido un valor no numérico.")
    except ZeroDivisionError:
        print("Error: No es posible dividir por cero.")
    else:
        print(f"El resultado es: {resultado}")
        print("La división fue exitosa.")

dividir_numeros()

#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()

def filtrar_mascotas_prohibidas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    resultado = filter(lambda x: x not in prohibidas, lista_mascotas)
    return list(resultado)

mis_animales = ["Perro", "Mapache", "Gato", "Tigre", "Canario", "Oso"]
animales_legales = filtrar_mascotas_prohibidas(mis_animales)
print(f"Mascotas permitidas: {animales_legales}")

#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    pass

def calcular_promedio(lista):
    if len(lista) == 0:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    return sum(lista) / len(lista)

numeros = [5, 10, 25]
try:
    resultado = calcular_promedio(numeros)
    print(f"El promedio es: {resultado}")
except ListaVaciaError as e:
    print(f"Error: {e}")  

#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    try:
        entrada = input("Por favor, introduce tu edad: ")
        edad = int(entrada)
        if 0 <= edad <= 120:
            print(f"Edad registrada correctamente: {edad} años.")
        else:
            print("Error: La edad debe estar entre 0 y 120 años.")  
    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un número entero.")

pedir_edad()

#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    palabras = frase.split()
    resultado = list(map(len, palabras))
    return resultado

texto = "Me gusta Python"
print(longitud_palabras(texto))

#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
#mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

def procesar_caracteres(caracteres):
    letras_unicas = set(caracteres.lower())
    resultado = list(map(lambda c: (c.upper(), c.lower()), letras_unicas))
    return resultado

entrada = "Ornitorrinco"
print(procesar_caracteres(entrada))

#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. 
# Usa la función filter()

def filtrar_por_letra(lista_palabras, letra):
    letra = letra.lower()
    resultado = list(filter(lambda p: p.lower().startswith(letra), lista_palabras))
    return resultado

palabras = ["Madrid", "Barcelona", "Pekín", "Praga", "Kiev"]
print(filtrar_por_letra(palabras, "p"))

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

def sumar_tres_a_lista(lista):
    return list(map(lambda x: x + 3, lista))

numeros = [10, 20, 30]
print(sumar_tres_a_lista(numeros))

#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#todas las palabras que sean más largas que n. Usa la función filter()

def filtrar_palabras_largas(texto, n):
    palabras = texto.split()
    resultado = list(filter(lambda p: len(p) > n, palabras))
    return resultado

frase = "Me voy de vacaciones a Praga"
print(filtrar_palabras_largas(frase, 5))

#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
#corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def lista_a_numero(digitos):
    # El acumulador se multiplica por 10 para desplazar el dígito a la izquierda
    # antes de sumar el siguiente (ej: 5 -> 50 + 7 = 57).
    resultado = reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)
    return resultado

numeros = [5, 7, 2]
print(lista_a_numero(numeros))

#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
#90. Usa la función filter()

def filtrar_estudiantes_excelentes(estudiantes):
    resultado = list(filter(lambda e: e["calificación"] >= 90, estudiantes))
    return resultado

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificación": 85},
    {"nombre": "Luis", "edad": 22, "calificación": 92},
    {"nombre": "Marta", "edad": 21, "calificación": 90},
    {"nombre": "Juan", "edad": 19, "calificación": 78}
]

print(filtrar_estudiantes_excelentes(estudiantes))

#19. Crea una función lambda que filtre los números impares de una lista dada.

def filtrar_impares(lista):
    return list(filter(lambda x: x % 2 != 0, lista))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtrar_impares(numeros))

#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función 
#filter()

def extraer_enteros(lista):
    # Es necesario 'not isinstance(x, bool)' porque en Python, 
    # la clase bool hereda de int (True == 1), y queremos excluir los booleanos.
    resultado = list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), lista))
    return resultado

mezcla = [10, "Madrid", 5, "Barcelona", 20, "Praga", 30]
print(extraer_enteros(mezcla))

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def calcular_cubo(numero):
    cubo = lambda x: x ** 3
    return cubo(numero)

print(calcular_cubo(3))

#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().

from functools import reduce

def producto_total(lista):
    resultado = reduce(lambda x, y: x * y, lista)
    return resultado

numeros = [1, 2, 3, 4, 5]
print(producto_total(numeros))

#23. Concatena una lista de palabras. Usa la función reduce() .

from functools import reduce

def concatenar_palabras(lista):
    resultado = reduce(lambda x, y: x + y, lista)
    return resultado

palabras = ["Hola", "que", "tal"]
print(concatenar_palabras(palabras))

#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

def diferencia_total(lista):
    resultado = reduce(lambda x, y: x - y, lista)
    return resultado

numeros = [100, 20, 10, 5]
print(diferencia_total(numeros))

#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    return len(texto)

cadena = "Barcelona"
print(contar_caracteres(cadena))

#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

def calcular_resto(a, b):
    resto = lambda x, y: x % y
    return resto(a, b)

print(calcular_resto(10, 3))

#27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista):
    return sum(lista) / len(lista)

numeros = [10, 20, 30, 40, 50]
print(calcular_promedio(numeros))

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada

def buscar_primer_duplicado(lista):
    vistos = set() # Usamos un conjunto (set) para búsqueda O(1) eficiente
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

numeros = [1, 2, 3, 4, 2, 5, 3]
print(buscar_primer_duplicado(numeros))

#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
#carácter '#', excepto los últimos cuatro.

def enmascarar_variable(valor):
    cadena = str(valor)
    if len(cadena) <= 4:
        return cadena
    
    mascara = "#" * (len(cadena) - 4)
    ultimos_cuatro = cadena[-4:]
    return mascara + ultimos_cuatro

entrada = "123456789"
print(enmascarar_variable(entrada))

#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#pero en diferente orden.

def es_anagrama(palabra1, palabra2):
    p1 = palabra1.lower().replace(" ", "")
    p2 = palabra2.lower().replace(" ", "")
    return sorted(p1) == sorted(p2)

print(es_anagrama("Roma", "Amor"))
print(es_anagrama("Hola", "Adios"))

#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#lanza una excepción.

def buscar_nombre():
    entrada = input("Introduce una lista de nombres separados por comas: ")
    lista_nombres = [nombre.strip() for nombre in entrada.split(",")]
    
    nombre_buscar = input("Introduce el nombre que deseas buscar: ")
    
    if nombre_buscar in lista_nombres:
        print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
    else:
        raise Exception(f"Error: El nombre '{nombre_buscar}' no se encuentra en la lista.")

buscar_nombre()

#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
#no trabaja aquí.

def buscar_puesto_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return empleado["puesto"]
    
    return "La persona no trabaja aquí"

empleados = [
    {"nombre": "Juan Pérez", "puesto": "Analista"},
    {"nombre": "Ana García", "puesto": "Desarrolladora"},
    {"nombre": "Luis López", "puesto": "Gerente"}
]

print(buscar_puesto_empleado("Ana García", empleados))
print(buscar_puesto_empleado("Samuel Delgado", empleados))

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas

def sumar_listas(lista1, lista2):
    # map acepta múltiples iterables; la lambda interna recibe (x, y) 
    # tomando un elemento de cada lista simultáneamente.
    sumar_elementos = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))
    return sumar_elementos(lista1, lista2)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
print(sumar_listas(lista_a, lista_b))

#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
#manipular la estructura del árbol.

class Arbol:
    def __init__(self):
        # 1. Inicializar con tronco de longitud 1 y lista de ramas vacía
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # 2. Aumentar longitud del tronco en una unidad
        self.tronco += 1

    def nueva_rama(self):
        # 3. Agregar nueva rama de longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # 4. Aumentar en una unidad la longitud de todas las ramas
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        # 5. Eliminar rama en una posición específica (ajustado a índice 0)
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Error: La posición de la rama no existe.")

    def info_arbol(self):
        # 6. Devolver información detallada
        return {
            "Longitud del tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitud de las ramas": self.ramas
        }

# --- Caso de Uso ---

# 1. Crear un árbol
mi_arbol = Arbol()

# 2. Hacer crecer el tronco una unidad
mi_arbol.crecer_tronco()

# 3. Añadir una nueva rama
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas una unidad
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2
# Nota: Usamos el índice 2 (que es la tercera rama)
mi_arbol.quitar_rama(2)

# 7. Obtener información
print(mi_arbol.info_arbol())

#36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
#corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
#agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta):
        # 1. Inicializar usuario
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta = tiene_cuenta

    def retirar_dinero(self, cantidad):
        # 2. Retirar dinero con validación
        if cantidad > self.saldo:
            raise ValueError(f"Error: {self.nombre} no tiene saldo suficiente para retirar {cantidad}.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}. Nuevo saldo: {self.saldo}")

    def agregar_dinero(self, cantidad):
        # 4. Agregar dinero al saldo
        self.saldo += cantidad
        print(f"Se han agregado {cantidad} a {self.nombre}. Nuevo saldo: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        # 3. Transferencia desde otro_usuario hacia self
        print(f"Intentando transferir {cantidad} desde {otro_usuario.nombre} a {self.nombre}...")
        
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"Error: {otro_usuario.nombre} no tiene saldo suficiente para transferir.")
        
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)
        print("Transferencia completada con éxito.")

# --- Caso de Uso ---

# 1. Crear dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo a "Bob"
bob.agregar_dinero(20)

# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia"

try:
    alicia.transferir_dinero(bob, 80)
except ValueError as e:
    print(e)

# 4. Retirar 50 unidades de saldo a "Alicia"
alicia.retirar_dinero(50)

#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , 
#reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
#de la función procesar_texto .

# 1. Función para contar palabras
def contar_palabras(texto):
    palabras = texto.split()
    resultado = {}
    for p in palabras:
        palabra_limpia = p.strip(",.")
        resultado[palabra_limpia] = resultado.get(palabra_limpia, 0) + 1
    return resultado

# 2. Función para reemplazar una palabra por otra
def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)

# 3. Función para eliminar una palabra
def eliminar_palabra(texto, palabra):
    return texto.replace(palabra, "").replace("  ", " ").strip()

# 4. Función principal que orquestra las demás
def procesar_texto(texto, opcion, *args):
    # Usamos *args para desempaquetar parámetros variables, ya que
    # 'reemplazar' necesita 2 argumentos extra y 'eliminar' solo 1.
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida"

# --- Caso de uso con ciudades ---
frase_viaje = "Me voy de viaje a Barcelona, Madrid y Praga."

print("Resultado Contar:", procesar_texto(frase_viaje, "contar"))
print("Resultado Reemplazar:", procesar_texto(frase_viaje, "reemplazar", "Barcelona", "Roma"))
print("Resultado Eliminar:", procesar_texto(frase_viaje, "eliminar", "Madrid"))

#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def informar_momento_dia(hora):
    if 6 <= hora <= 12:
        return "Es de día"
    elif 13 <= hora <= 20:
        return "Es por la tarde"
    elif (21 <= hora <= 23) or (0 <= hora <= 5):
        return "Es de noche"
    else:
        return "Hora no válida (debe ser entre 0 y 23)"

try:
    entrada = int(input("Introduce la hora (0-23): "))
    print(informar_momento_dia(entrada))
except ValueError:
    print("Por favor, introduce un número entero válido.")

#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.

def evaluar_calificacion(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Error: La calificación debe estar entre 0 y 100"

try:
    puntuacion = float(input("Introduce la calificación numérica del alumno: "))
    resultado = evaluar_calificacion(puntuacion)
    print(f"El alumno tiene un desempeño: {resultado}")
except ValueError:
    print("Por favor, introduce un número válido.")

#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o 
#"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    figura = figura.lower()
    
    if figura == "rectangulo":
        # Desempaquetado de tupla: asignamos los valores directamente a variables
        base, altura = datos
        return base * altura
    
    elif figura == "circulo":
        radio = datos[0]
        return math.pi * (radio ** 2)
    
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    
    else:
        return "Figura no reconocida"

print(f"Área del Rectángulo (10x5): {calcular_area('rectangulo', (10, 5))}")
print(f"Área del Círculo (radio 7): {calcular_area('circulo', (7,))}")
print(f"Área del Triángulo (base 6, altura 8): {calcular_area('triangulo', (6, 8))}")

#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
#monto final de una compra en una tienda en línea, después de aplicar un descuento. 

def calcular_total_compra():
    # 1. Solicitar el precio original
    try:
        precio_original = float(input("Introduce el precio original del artículo: "))
        
        # 2. Preguntar por el cupón
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").lower().strip()

        if tiene_cupon == "sí" or tiene_cupon == "si":
            # 3. Solicitar el valor del cupón
            valor_cupon = float(input("Introduce el valor del cupón de descuento (en €): "))
            
            # 4. Validar el cupón y aplicar el descuento
            if valor_cupon > 0:
                if valor_cupon <= precio_original:
                    precio_final = precio_original - valor_cupon
                else:
                    print("El cupón supera el precio; el artículo será gratuito.")
                    precio_final = 0
            else:
                print("El cupón no es válido (debe ser mayor a cero).")
                precio_final = precio_original
        
        elif tiene_cupon == "no":
            precio_final = precio_original
        
        else:
            print("Opción no reconocida. Se procederá sin descuento.")
            precio_final = precio_original

        # 5. Mostrar el precio final
        print(f"\n--- Resumen de Compra ---")
        print(f"Precio original: {precio_original}€")
        print(f"Precio final: {precio_final}€")

    except ValueError:
        print("Error: Por favor, introduce valores numéricos válidos.")

calcular_total_compra()