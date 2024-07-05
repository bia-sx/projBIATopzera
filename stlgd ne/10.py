"""Elabore uma função que receba dois números inteiros positivos por parâmetros e retorne a
soma dos N números inteiros existentes entre eles.
"""
def bilu(p1,p2):
    if p1>=0:
        print(f"positivo é {p1}")
    elif p2>=0:
        print(f"positivo é {p2}")  
    else:
        print("não esistente")
bilu(-1,2)              