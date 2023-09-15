#!/bin/env python3

""" Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala que frequentam
cada uma das atividades
"""
__version__ = "0.1.1"


atividades = {
    'Ingles': ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    'Musica': ["Erik", "Carlos", "Maria"],
    'Danca': ["Gustavo", "Sofia", "Joana", "Antonio"]
}

salas = {
    'sala1': ["Erik", "Maia", "Gustavo", "Manoel", "Sofia", "Joana"],
    'sala2': ["João", "Antonio", "Carlos", "Maria", "Isolda"]
}


for nome_atividade, alunos_na_atividade in atividades.items():  # separando chave(atividade) e valor(alunos)
        print(f"Alunos da atividade {nome_atividade}\n")  #imprimi chave(atividade)
        print("-" * 40)

        for nome_sala, alunos_na_sala in salas.items():  #separando chave(nome_sala) e valor(alunos_na_sala)
            alunos_comuns = set(alunos_na_atividade) & set(alunos_na_sala)
            print(f"{nome_sala}: {alunos_comuns}")

        print("-" * 40)

