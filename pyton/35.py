valor=int(input("\ndigite o valor da venda:"))

num1=700+ (valor*16)/100
num2=650+(valor*14)/100
num3=600(valor*14)/100
num4=550(valor*14)/100
num5=500(valor*14)/100
num6=400(valor*14)/100

if valor>=100.000:
   print(f"a sua comisao sera de {num1}reais")

elif 100.000>valor>=80.000:
  print(f"a sua comisao sera{num2}reais")

elif  80.000>valor>=60.000:
   print(f"a sua comisao sera{num3}reais")

elif 60.000>valor>=40.000:
   print(f"a sua comisao sera de{num4}reais")

elif 40.000>valor>=20.000:
   print(f"o valor da sua comisao sera de{num5}reais")

elif valor> 20.000 :
   print(f"a sua comisao sera de {num6}reais") 
       