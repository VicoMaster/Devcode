# coding: utf-8
"""
Funciones anonimas, on the go, on demand, online
"""
# Esta utilización no la acepta pep8
def area_triangulo(base, altura): return (base * altura) / 2


triangulo1 = area_triangulo(7, 5)
print(triangulo1)
# Esta utilización no la acepta pep8
def destacar_valor(comision): return "¡{}! $".format(comision)


comision_ana = 15532
print(destacar_valor(comision_ana))

# Uso 1
numeros = [14, 25, 36, 32, 52, 99]
print(list(filter(lambda numero: numero % 2 == 0, numeros)))

# Uso 2


class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${} USD".format(self.nombre, self.cargo, self.salario)


lista_empleados = [
    Empleado("Juan", "Director", 750_000),
    Empleado("Ana", "Presidenta", 850_000),
    Empleado("Antonio", "Administrativo", 25_000),
    Empleado("Sara", "Secretaria", 27_000),
    Empleado("Mario", "Botones", 21_000),
    Empleado("Rodrigo", "Conductor", 10_000),
]

salarios_altos = filter(
    lambda empleado: empleado.salario > 50_000, lista_empleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)
