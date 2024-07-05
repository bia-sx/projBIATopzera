num1 = int(input(" trabalho: "))
num2 = int(input(" avaliação: "))
num3 = int(input(" exame final: "))


if 0 <= num1 <= 10: 
    if 0 <= num2 <= 10:
        if 0 <= num3 <= 10:
            fnl = (num1 * 0.2 + num2 * 0.3 + num3 * 0.5)
            print(f"A média destas notas é {fnl:.1f} pontos")
            if fnl <= 3:
                print(" REPROVADO")
            elif fnl <= 5.9:
                print("recuperação")
            else:
                print(" está APROVADO")
        else:
            print("inválida")
    else:
        print(" inválida")
else:
    print(f" inválida")