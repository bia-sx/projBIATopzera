#Um pescador, comprou um PC para controlar o rendimento diári de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
"""estabelecido pelo regulamento de pesca do MS (50 Kg) deve pagar
uma multa de R$ 4,00 por quilo excedente. O pescador precisa que
você crie uma função para ler a quantidade de peixes e calcular o
excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que o pescador deverá
pagar. Imprima os dados do programa com as mensagens adequadas."""

def cinto (p1):
   p1=(input("quanto foi pescado?"))
   multa =(p1^4)
   if p1 <=50:
      print("que bom!!voce nao pagara multa")
   else:
      print(f"vai pagar uma multaa de {multa} ")

