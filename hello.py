#!/usr/bin/env python3 # Shebang é #! especifica interpretador especifico
"""Hello World Multi lingua

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar: 

tenha a variável lang devidamente configurada

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
    
"""


__version__ = "0.1.2"
__author__ = "John Caracho"
__license__ = "Unlicense"

import os  #modulo tem a funcionalidade de ler variaveis de ambiente do sistema operacional
# Dunder significa indentificado __ (dois underline)


current_language = os.getenv("LANG", "en_US")[:5] # após a virgula significa que o valor padrão será en_US e pega os 5 primeiro caracteres

msg = {
    "pt_BR": "Olá', Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola Mundo!",
    "fr_FR": "Bonjour le monde!",
    "en_US": "Hello, World"
}

# O (1) velocidade constante
print(msg[current_language])

