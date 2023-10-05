#!/usr/bin/env python3
"""Calculadora prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50
$ prefixcalc.py
operacao: sum
n1: 5
n2: 4
9

Os resultados serao salvo em prefixcalc.log
"""
import sys
import os
from datetime import datetime
__version__ = "0.1.0"
import sys
arguments = sys.argv[1:] # caso vazio será false

if not arguments:
    operation = input("operação: ")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: 'sum 5 5' ")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validate_nums = [] # cria lista pra acumular os numeros depois de serem validados

for num in nums:
    # TODO: Repetiçao com while + exception
    if not num.replace(".", "").isdigit():
        print(f"Número invalido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
        print(num)
    else:
        num = int(num)
    validate_nums.append(num)

n1, n2 = validate_nums
# TODO Usar dict de funçoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

with open(filepath, "a") as file_:  # feito file_ pois file é usado pelo python2
    file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
print(f"O resultado é {result}")



# minha tentativa
# operacoes = {"sum": None, "sub": None, "mul": None, "div": None}
# operador = sys.argv[1]
# n1 = int(sys.argv[2])
# n2 = int(sys.argv[3])
#
# if operador == "sum":
#     resultado = n1 + n2
#     print(f"valor da soma é: {resultado}")
#
# if operador == "sub":
#     resultado = n1 - n2
#     print(f"valor  é: {resultado}")
#
# if operador == "mul":
#     resultado = n1 * n2
#     print(f"valor é: {resultado}")
#
# if operador == "div":
#     resultado = n1 / n2
#     print(f"valor é: {resultado}")