enpresa={'nome':'genio/cranio','uni':'fone','email':'cidade''racunamatata','uf':'sequiseresimman'}
pdp=[]
uni=[]
emails=[]
for i in range (4):
    enpresa['nome']=input("\nnome de empresa: ")
    enpresa['uni']=input("\nunidade:")
    enpresa['fone']=input("\ntelefone:")
    enpresa['email']=input("\nemail: ")
    enpresa['cidade']=input("\nsua cidade: ")
    enpresa['uf']=input("\nseu uf seria: ")
    print(enpresa)
    uni.append(enpresa['uni'])
    emails.append(enpresa['email'])
   
        