nome=(input("\npor favor digite seu nome : "))

matricula=(input("\n informe se voce possui matricula: ")).lower()


if matricula =="sim" or matricula =="possuo":
    print(f"\n ok. agora por favor Sr.{nome} coloque a senha de acesso")
    senha=int(input("\nsenha:")) 
    senha=54885


elif matricula == "não" :
    print(f"\n ok.{nome} vamos fazer a matricula, preencha o espaço abaixo:")
    matricula2=(input("digite seu Email:"))
    nomec=(input("digite seu nome completo:"))
    print(f"ok.{nomec} enviaremos no email com a senha de acesso. por favor aguarde")

else :
    print("não correspondido")    


    





