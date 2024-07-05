"""Escreva uma função que receba como parâmetro a quantidade de alunos para apresentar um
trabalho. Esta função deve solicitar ao usuário os nomes de alunos de uma sala de aula. Após
cadastrar a quantidade informada de alunos a função deve sortear e retornar para o usuário o
aluno(a) que irá apresentar o trabalho primeiro. Exemplo:
sorteiaAluno(6)
Digite um nome: Guilherme
Digite um nome: Eduardo
Digite um nome: Gisele
Digite um nome: Matheus
Digite um nome: João
Digite um nome: Duda
O primeiro aluno(a) a apresentar será: Gisele"""


import random

def eminem(p1):
    alunos = []
    
    for _ in range(p1):
        nome = input("Digite um nome: ")
        alunos.append(nome)
    
    
    individuo = random.choice(alunos)
    
   
    print(f"O primeiro aluno(a) a apresentar será: {individuo}")


eminem(6)