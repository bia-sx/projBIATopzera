#criar uma lista com 6 números inteiros
lista = [4,7,2,9,5,1]
 
#adiconar 6 números decimais a lista
lista.extend([3.5,6.8,1.2,8.9,4.7,2.1])
 
#remover os dois últimos itens da lista
del lista[-2:]
 
#adicionar 10 e 11 na posição 1 e 2 da lista
lista.insert(1, 10)
lista.insert(2, 11)
 
#ordenar a lista em ordem crescente
lista.sort()
 
#imprimir o maior número da lista
print("O MAIOR NÚMERO DA LISTA É: ", max(lista))
 
#imprimir o meno número da lista
print("O MENOR NÚMERO DA LISTA É: ", min(lista))
 
#imprimir a soma dos itens da lista
print("A SOMA DOS ITENS DA LISTA É: ", sum(lista))
 
#imprimir a média dos itens da lista
media = sum(lista) / len(lista)
print("A MÉDIA DOS ITENS DA LISTA É: ", media)
 
#remover o número 10 e imprimir o índice do 11
lista.remove(10)
indice_11 = lista.index(11)
print("O ÍNDICE DO NÚMERO 11 NA LISTA É: ", indice_11)
 
#multiplicar o quinto pelo sexto elemento da lista
produto = lista[5] * lista[6]
print("O PRODUTO DO QUINTO PELO SEXTO ELEMENTO É: ", produto)
 
#imprimir a lista em ordem decrescente
lista.sort(reverse = True)
print("A LISTA EM ORDEM DECRESCENTE É: ", lista)