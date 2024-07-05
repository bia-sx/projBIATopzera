num=float(input("\ndigite o valor do produto:"))
a=num+(num*0.45)
b=num+(num*0.30)
if num <50.00:
 print(f"o preco do produto devera ser vendido por {a} a mais ")
else:
   print(f"entao o lucro sera de {b} a mais ")
