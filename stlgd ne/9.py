"""Elabore uma função que receba dois valores numéricos e um símbolo. Este símbolo representara
a operação que se deseja efetuar com os números. Se o símbolo for + deverá ser realizada uma
adição, se for * uma subtração, se for / uma divisão e se for * será efetuada uma multiplicação."""
def pec(p1,p2,s):
    if s=="*":
        a=p1*p2
    elif s=="-" :
           b=p1 -p2
    elif s==  "+":
         c=p1 + p2
    elif s == "/"  :
         d=p1 /p2
    print(pec(p1,p2,s))
    p1=(input("qual é o primeiro numero:")) 
    p2=(input("qual é o segundo numero"))  
    s= (input("qual será a operação:"))  
