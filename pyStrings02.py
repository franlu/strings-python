#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Se leen 50 caracteres y se eliminan todos los separadores. Se
consideran separadores espacios en blanco, tabuladores y retorno"""


input_str = raw_input('Escribe un máximo de 50 caracteres: ')

while len(input_str) > 50:
    print "Error, solo se permiten un total de 50 caracteres."
    input_str = raw_input('\nIntentalo de nuevo: ')

SEPARATORS = ' \t\n'

print "Cadena CON separadores: ", input_str

print "\nCadena SIN separadores: ", input_str.translate(None, SEPARATORS)
