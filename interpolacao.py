#!/usr/bin/env python3
email_tmpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?

Este produto é ótimo, %(texto)s
Clique agora em %(link)s

e corra apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f
 """


clientes = ["Maria", "João", "Bruno"]

for cliente in clientes:
     print(email_tmpl % {"nome": cliente, "produto": "caneta azul", "texto": "Escreve muito bem",
     "link": "https://canetas.com", "quantidade": 1, "preco":  50.5})


     
