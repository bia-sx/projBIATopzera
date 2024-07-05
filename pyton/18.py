num = float(input("\ndigite sua altura: "))
num2 = int(input("\ndigite o seu sexo obs: so pode ser masculino ou feminino: "))

a = (72.7*num) - 58
b= (62* num) - 44.7

if num == "feminino":
    print(f"o seu peso ideial seria de {b} ok")
elif num =="masculino":
     print(f"o seu peso ideal seria de {a} ok")     
else:
     print("vc n sabe ler nao") 