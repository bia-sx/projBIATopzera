print("bom dia, por favor escolha uma operação para iniciarmos as equações:")
print("1 - soma")
print("2 - subtracao")
print("3 - multiplicacao")
print("4 - divisao")

opcao = int(input("digite o número da operação desejada: "))

valor1 = float(input("digite o primeiro valor: "))
valor2 = float(input("digite o segundo valor: "))

if opcao == 1:
    resultado = valor1 + valor2
    print(f"o resultado da soma é: {resultado}")

elif opcao == 2:
    resultado = valor1 - valor2
    print(f"o ressultado da subtração é: {resultado}")

elif opcao == 3:
    resultado = valor1 * valor2
    print(f"o resultado da multipicação é: {resultado}")

elif opcao == 4:
    if valor2 != 0:
        resultado = valor1 / valor2 
        print(f"o resultado da divisão é: {resultado}")
    else:
        print("IMPOSSÍVEL DIVIDIR POR ZERO!")
else:
    print("OPÇÃO INVÁLIDA!")