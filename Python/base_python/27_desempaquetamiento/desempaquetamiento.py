# Desenpaquetamiento en Python
# coding: utf-8

lista = [1, 3, 4, 5, 6, "nada"]


def desempaquetamiento(var1, var2, var3, var4, *args):
    print("Variables: %i" % var1, var2, var3, var4)  # En parametros
    print(args)  # Argumentos sobrantes


def desempaquetamiento_dict(clave1, clave2, clave3, clav4=None, **kwargs):
    print("Variables posicionales: %s" % clave1, clave2, clave3, clav4)
    print(kwargs)


print("DESEMPACANDO LISTA: ")
desempaquetamiento(*lista)
print("DESEMPACANDO DICCIONARIO: ")
diccionario = {
    "clave1": 10,
    "clave2": 20,
    "clave3": 30,
    "clave4": 40,
    "clave5": "Fuera de Rango"
}
# Se hace un pasado de argumentos nominales por desempaquetado
desempaquetamiento_dict(**diccionario)

# Desempaquetado formando un diccionario
print("REFORMANDO Y DESEMPAQUETANDO ***")
desempaquetamiento_dict(**dict(zip(("clave1", "clave2", "clave3", "clav4", "5", "6"), lista)))

# Uso de ZIP
alumnos = ['Andres', 'Felipe', 'Maria', 'Loreto']
edades = [28,27,25,26,99]
notas = [1.5,2.8,4.8,5.0]
datos_alumnos = zip(alumnos, edades, notas)
# Imprimiendo Dict
print(datos_alumnos)
# Imprimiendo objeto convertido en lista
print(list(datos_alumnos))

# DATO IMPORTANTE -> Si se recorre y se vacía el iterador del ZIP, luego no tendrá elementos
alumnos = ['Andres', 'Felipe', 'Maria', 'Loreto']
notas = [1.5,2.8,4.8,5.0]
nueva_lista = zip(alumnos,notas)
for grupo in nueva_lista:
    print(grupo)

print('---->{}'.format(list(nueva_lista)))
