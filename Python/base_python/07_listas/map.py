# -*- coding: utf-8 -*-
""" 
    Autor: AndrésR.Dev
    Description: Uso de Map para unir 2 listas
    Logic: 2 listas de entrada, lambda para retornar una sola lista unida

"""

names_list = ['Andres', 'Maria', 'Felipe', 'Loreto']
lastnames_list = ['Rivera', 'Moya', 'Lozano', 'Alvarez']

# Unimos las listas

persons_list = list(
    map(lambda nombre, apellido: f'{nombre} {apellido}', names_list, lastnames_list))
print(persons_list)
