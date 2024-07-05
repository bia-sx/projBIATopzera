#projeto da enilda pdp
#tem q adiciona,atualiza e incluir pdp
#


num1 = []
nomesito = []
prexxo = []
descrever = []
estoque= []
utilizar= []
digitado = len(utilizar)





#meu deus que bagulho dificio 
def input2(mensagem = "", varialvel = str):
    while True:
        try:    
            ret = varialvel(input(mensagem))
            return ret
        except ValueError:
            print("Valor inserido é invalido", end=' ')
 
#apartir daqui e vapo
while True:
    print("\n\nQual ação você deseja realizar? ")
  
    print(" [01] coloca produto")
    
    print(" [02]  quantidade ")

    print(" [03] analisar  os produtos")

    print(" [04] descrição ")

    print(" [05] Atualizar ")
 
    acao = input2("     ", int)
    if acao == 0:
        break
    elif acao == 1:
        print(f"O código do seu produto será: {digitado}")


 
        nome = input2("coloca o nome : ")
        preco = input2("preço: ", float)
        desc = input2(" descrição : ")
        qtd = input2("quantidade no estoque: ", int)



 
        num1.append(digitado)
        nomesito.append(nome)
        prexxo.append(preco)
        descrever.append(desc)
        estoque.append(qtd)
        prod = [digitado, nome, preco, desc, qtd]
        utilizar.append(prod[:])

 
        digitado += 5


 
    elif acao == 2:
        if len(utilizar) == 0:
            print("Não há ")
        else:
            cod = input2("coloca o código pra ser atualizado: ", int)
            if cod in num1:
                #da pra enfiar variavel aqui??

               
                ind = num1.index(cod)
                mens = f"Digite o novo nome de {nomesito[ind]}: "
                n_nome = input2(mens)
                mens = f"Digite o novo preço [R${prexxo[ind]:.2f}]: "
                n_preco = input2(mens, float)
                mens = f"Digite a nova descrição: "
                n_desc = input2(mens)
                mens = f"Digite a nova quandidade de itens [{estoque[ind]}]: "
                n_qtd = input2(mens, int)
 
                n_prod = [cod, n_nome, n_preco, n_desc, n_qtd]
                nomesito[ind] = n_prod[1]
                prexxo[ind] = n_prod[2]
                descrever[ind] = n_prod[3]
                estoque[ind] = n_prod[4]


 
                utilizar[ind] = n_prod


 
            else:
                print("inesistemte")
    elif acao == 3:
        for i in range(len(num1)):
            print(f"Quantia de {nomesito[i]}:     {estoque[i]}")
    elif acao == 4:
        for it in utilizar:
            print(f" Código: {it[0]}")
            print(f" produto: {it[1]}")
            print(f"Preço : R${it[2]:.2f}")
            print(f"Descrição : {it[3]}")
            print(f"Quantidade : {it[4]}")
            print("#"*50)