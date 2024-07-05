"""Elabore uma função que receba dois números inteiros como parâmetros e inicialize uma
matriz preenchidas de 1 de acordo com os valores recebidos, exemplo:
criaMatriz(3,3)
[[1, 1, 1],
[1, 1, 1],
[1, 1, 1]]
"""

def kiss(linhas, colunas):
    matriz = [[1 for _ in range(colunas)] for _ in range(linhas)]
    return matriz


linhas = 3
colunas = 3
matriz = kiss(linhas, colunas)
for linha in matriz:
    print(linha)