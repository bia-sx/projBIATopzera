salario = int(input("\no salario de um trabalhado:"))
parcela = int(input("\no salario do imprestimo:"))

porcentagem = salario * 0.20

if parcela > porcentagem:
    print("NAO PODE TIRAR EMPRESTIMO")
else:
    print("EMPRESTIMO CONCEDIDO!!!")

