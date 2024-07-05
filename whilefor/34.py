num=[]
par=[]
impar=[]

for i in range(20):
    chuchu=int(input("digita ai!"))

    if chuchu % 2 == 0:
        par.append (chuchu)


    else :
        impar.append (chuchu)

    num.append(chuchu)

print (f"Os números pares digitados foram:{par}\nOs numeros impares digitados foram: {impar}")
      
