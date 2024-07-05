#BAGULHO DO ESTOQUE
#AAAAAAAAAAAAAAAA COMO EU VO FAZER????????
#AAAAAAAAAAAAAAAAA
estoque=[]
nomesito = []
prexo = []
estoq_l = []
num1= len(estoque)
def input2(mensagem = "", varialvel = str):
    while True:
        try:    
            ret = varialvel(input(mensagem))
            return ret
        except ValueError:
            print("Valor inserido é invalido", end=' ')
while True:
    print("o que vai pra hoje ?")
    print("[A] colocar produto!")
    print("[b] atualizar os estoque!")
    print("[c]ver quantidade!")
   
   
    num= input2("     ", int)
    if num == 0:
        break
    elif num==" A": 
        print(f"O código do seu produto será: {num1}")

        nome = input("Digite o nome do produto a ser adicionado: ")
        preco = input("Digite o preço do produto: ", float)
       
        qtd = input("Digite a quantidade do estoque deste item: ", int)

        num1.append(num1)
        nomesito.append(nome)
        prexo.append(preco)
        
        estoque.append(qtd)
        prod = [num1, nome, preco,  qtd]
        estoque.append(prod[:])
        num1+= 5
 
    elif num == 2:
        if len(estoque) == 0:
            print("Não há cadastro")
        else:
            cod = input2("atualize: ", int)
            if cod in num1:
                # print("este item existe")
                # esta parte está mal optimizada, entretanto funciona
               
                ind = num1.index(cod)
                mens = f"Digite o novo nome de {nomesito[ind]}: "
                n_nome = input2(mens)
                mens = f"Digite o novo preço [R${prexo[ind]:.2f}]: "
                n_preco = input2(mens, float)
                mens = f"Digite a nova descrição: "
                n_desc = input2(mens)
                mens = f"Digite a nova quandidade de itens [{estoq_l[ind]}]: "
                n_qtd = input2(mens, int)
 
                n_prod = [cod, n_nome, n_preco, n_desc, n_qtd]
                nomesito[ind] = n_prod[1]
                prexo[ind] = n_prod[2]
                
                estoque[ind] = n_prod[4]
 
                estoque[ind] = n_prod
 
            else:
                print("não tem")
    elif num == 3:
        for i in range(len(num1)):
            print(f"Quantidade de {nomesito[i]}:     {estoq_l[i]}")
    elif num == 4:
        for it in num:
            print(f" Código: {it[0]}")
            print(f"Nome do produto: {it[1]}")
            print(f"Preço do item: R${it[2]:.2f}")
          
            print(f"Quantidade em estoque: {it[4]}")
            print("#"*50)
 
        
 


     