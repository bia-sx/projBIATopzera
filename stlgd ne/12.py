"""Elabore uma função que receba a distância em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma
mensagem de acordo com a tabela abaixo:
Consumo Km/l Mensagem
menor que 8 Gasta muito!
entre 8 e 15 Econômico!
maior que 15 Super econômico"""
"""sim= (input("digite o valor gastado")"""
def oloco(p1):


 if p1 <=8:
        print("gasta muito!!!")
    
 elif p1 > 8 and p1 <= 15:
        print ("econômico!!")  
 elif p1 > 15 :
        print("super econômico!!")    
p1=(input("\ndigite o valor gastado:"))
oloco(p1)          
    