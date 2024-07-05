"""Escreva uma função que gera um triângulo lateral de altura 2*n-1 e n largura. Por exemplo, a
saída para n = 4 seria:"""
"""def sla(p1):
autura=(2*p1-1)"""
def sla(p1):
   
    for i in range(1, p1 + 1):
        print('*' * i)
    

    for i in range(p1 - 1, 0, -1):
        print('*' * i)


p1 = 4
sla(p1)