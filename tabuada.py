#!/usr/bin/env python3

"""Imprime a tabuada do 1 ao 10.
Tabuadda do 1
1
2
3

...
---------------
Tabuada do 
2
4
...

-------------

"""
__version__ = "o.1.0"
__author__ = "John"
numeros = list(range(1, 11))

# Iterable (percorrivel)
# para cada numero em numeros:
for numero in numeros:
    print("Tabuada do: ", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)        
    print("--------")









