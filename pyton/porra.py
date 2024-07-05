cod_l = []
nome_l = []
preco_l = []
descricao_l = []
estoq_l = []
itens = []
cod_g = len(itens)

def input2(mensagem = "", varialvel = str):
    while True:
        try:    
            ret = varialvel(input(mensagem))
            return ret
        except ValueError:
            print("Valor inserido é invalido", end=' ')

# B O G A
while True:
    print("\n\nQual ação você deseja realizar? ")
    print(" [0] encerrar o sistema")
    print(" [1] Adicionar item")
    print(" [2] Atualizar informações do item")
    print(" [3] ver quantidade de estoque")
    print(" [4] Ver todos os itens")
    print(" [5] Ver descrição de um item")
    print(" [6] Atualizar estoque")

    acao = input2("     ", int)
    if acao == 0:
        break
    elif acao == 1: 
        print(f"O código do seu produto será: {cod_g}")

        nome = input2("Digite o nome do produto a ser adicionado: ")
        preco = input2("Digite o preço do produto: ", float)
        desc = input2("Digite uma descrição para o produto: ")
        qtd = input2("Digite a quantidade do estoque deste item: ", int)

        cod_l.append(cod_g)
        nome_l.append(nome)
        preco_l.append(preco)
        descricao_l.append(desc)
        estoq_l.append(qtd)
        prod = [cod_g, nome, preco, desc, qtd]
        itens.append(prod[:]) 

        cod_g += 5

    elif acao == 2: 
        if len(itens) == 0:
            print("Não há itens cadastrados no sistema")
        else:
            cod = input2("Digite o código do item a ser atualizado: ", int)
            if cod in cod_l:
                # print("este item existe")
                # esta parte está mal optimizada, entretanto funciona
                
                ind = cod_l.index(cod)
                mens = f"Digite o novo nome de {nome_l[ind]}: "
                n_nome = input2(mens)
                mens = f"Digite o novo preço [R${preco_l[ind]:.2f}]: "
                n_preco = input2(mens, float)
                mens = f"Digite a nova descrição: "
                n_desc = input2(mens)
                mens = f"Digite a nova quandidade de itens [{estoq_l[ind]}]: "
                n_qtd = input2(mens, int)

                n_prod = [cod, n_nome, n_preco, n_desc, n_qtd]
                nome_l[ind] = n_prod[1]
                preco_l[ind] = n_prod[2]
                descricao_l[ind] = n_prod[3]
                estoq_l[ind] = n_prod[4]

                itens[ind] = n_prod

            else:
                print("Este item não existe")
    elif acao == 3:
        for i in range(len(cod_l)):
            print(f"Quantidade de {nome_l[i]}:     {estoq_l[i]}")
    elif acao == 4:
        for it in itens:
            print(f" Código: {it[0]}")
            print(f"Nome do produto: {it[1]}")
            print(f"Preço do item: R${it[2]:.2f}")
            print(f"Descrição do item: {it[3]}")
            print(f"Quantidade em estoque: {it[4]}")
            print("#"*50)