m=[]
for linha in range (5):
    lin=[]
    for coluna in range (5):
        if linha == coluna :
            lin.append(1)
        else:
            lin.append(0)
    m.append(lin)
for i in m:
    print(i)            
