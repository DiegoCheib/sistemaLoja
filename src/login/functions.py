#funcoes

import sqlite3

conn = sqlite3.connect('/home/roberto/Projects/sistema/src/db.sqlite3')
cursor = conn.cursor()

def search():
    table = input('Qual table deseja procurar:    ')
    cursor.execute(f'PRAGMA table_info({table});')
    describe = cursor.fetchall()
    lista_colunas = cleanPragma(describe)
    for colunas in lista_colunas:
        print(f"{colunas}   |   ", end='')
    coluna = input('\nBaseado em qual coluna deseja:    ')
    value = input('Valor da sua linha na coluna escolhida acima:    ')
    cursor.execute(f'SELECT * FROM {table} WHERE {coluna} = "{value}";')
    result = cursor.fetchall()
    print(result)


def cleanPragma(pragmaResult: list) -> list:
    lista_colunas = []
    for tuplas in pragmaResult:
        for elements in tuplas:
            index = tuplas.index(elements)
            if index == 1:
                lista_colunas.append(elements)
            else:
                continue
    return lista_colunas
                


search()
