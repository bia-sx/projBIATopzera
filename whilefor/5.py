ano = int(input("Digite o ano a ser analizado: "))

if ano % 4 == 0:
    if ano % 100 != 0 or ano % 400 == 0:
        print("O ano é bissexto")
    else:
        print("O ano não é bissexto")
else:
    print("O ano não é bissexto")
