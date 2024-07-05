"""Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1. Por exemplo, a
saída para n = 6 seria:"""

    
def lulu_santos (n):
    for i in range(1, n + 1):
        
        y= n - i
     
        x= 2 * i - 1
      
    linha = ' ' * y + '*' * x
    print(linha)


n = 19
lulu_santos(n)