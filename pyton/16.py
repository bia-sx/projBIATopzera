num = float(input("Quantas horas foram trabalhadas: "))

hora = 40.50

num2 = num * hora
print(num2)

if num2> 2500:
    num3= (num2* 11)/100
    num2 = num2 - num3

    print("O seu salário liquido com desconto ficou: ",num2)

else:
    print("O seu salário liquido foi: ", num2)