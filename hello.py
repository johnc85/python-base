#!/usr/bin/env python3 # Shebang é #! especifica interpretador especifico
"""Hello World Multi lingua

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar: 

tenha a variável lang devidamente configurada

    export LANG=pt_BR
Ou informe através do CLI --lange
Ou usuário terá que digitar
Execução:

    python3 hello.py
    ou
    ./hello.py
    
"""


__version__ = "0.1.3"
__author__ = "John Caracho"
__license__ = "Unlicense"

import os  #modulo tem a funcionalidade de ler variaveis de ambiente do sistema operacional
# Dunder significa indentificado __ (dois underline)
import sys
arguments = {"lang": None,  "count": 1}
for arg in sys.argv[1:]:
    # TODO: tratar ValueError
    key, value = (arg.split("="))
    key = key.lstrip("-").strip() #remove - da esquerda espacos em branco
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value
current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: usar repetiçao
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5] # pega so os 5 primeiros caracteres

msg = {
    "pt_BR": " Olá, Mundo!",
    "it_IT": " Ciao, Mondo!",
    "es_ES": " Hola Mundo!",
    "fr_FR": " Bonjour le monde!",
    "en_US": " Hello, World!"
}

# O (1) velocidade constante
print(msg
      [current_language] * int(arguments["count"]) # necessario converter para int pois os dados vindo do usuário sao tipo texto
)

