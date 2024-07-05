"""Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra
for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a
média ponderada, com pesos 5, 3 e 2."""

def guru(p1,p2,p3,l):
    ho=(p1+p2+p3)/3
    if l=="a":
        print(f"a sua media é:{ho} ")

