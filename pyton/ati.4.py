notasavali=int(input("\ndigite o numero de provas:"))
i=0

soma=0

while i < notasavali:

    soma+= float (input("\ndigite a nota:"))


    i=i+ 1

media = soma / notasavali

print(media)
