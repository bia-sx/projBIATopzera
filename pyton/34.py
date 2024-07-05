pa=float(input("\nigite o preco antigo:"))

num1=(pa*50)/100 #se ele for ate 50
num2=(pa*10)/100#se ele for de 50 a 100
num3=(pa*15)/100#se ele for acima de 100

if pa<=50:
    print(f"o valor do almento sera{num1}reais")
elif 50<pa<100:
    print(f"o valor do almento sera {num2}reais")
elif pa  >100:  
    print (f"o valor  do almento sera {num3}reais")  

