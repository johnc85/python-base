#!/usr/bin/env python3

"""Imprime a tabuada do 1 ao 10.
----Tabuadda do 1----
        1 X 1 = 2
        2 X 1 = 2
        3 x 1 = 3
...
####################
----Tabuada do  2 ----
        2 x 1 = 2
        2 x 2 = 4
        2 x 3 = 6 
...
####################

"""
__version__ = "o.1.0"
__author__ = "John"


# Iterable (percorrivel)
# para cada numero em numeros:
numeros = list(range(1, 11))
    

for n1 in numeros:
    print()
    print("{:<18}".format(f"Tabuada do {n1} \N{White Down Pointing Backhand Index}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("=" * 18)










