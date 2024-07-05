valora=int(input("\ndigite o seu antigo salario:"))
ts=int(input("\ndigite o seus anos de serviço na empresa:"))

num1=(500*25)/100
num2=(1000*20)/100
num3=(1500*15)/100
num4=(2000*10)/100

bonus1=num2 + 100
bous2=num3 + 200
bonus3=num4 + 300
bonus4=2000 + 500

if valora<=500:
    print(f"\ncom o reajuste o seu salario agora sera {num1}reais")

elif 500> valora>1000:
    print(f"\ncom o reajuste o seu salario seria {num2} , mas acrecentou um reajuste e ficara {bonus1}")  

elif 1000> valora>1500:
    print(f"\ncom o reajuste o seu salario seria {num3}, mas acrecentou um reajuste e ficara {bous2} ")

elif 1500 > valora > 2000 :
    print(f"\n com O Reajuste o seu salario seria {num4}, mas acrecentou um reajuste e ficara {bonus3} ")

elif valora  > 2000 :
    print(f"\n o seu salario nao ira ter reajuste so acrecimo e ficara de {bonus4}")

