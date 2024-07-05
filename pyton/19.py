n = int(input("Digite um número maior que 0: "))

if n > 0:
    val = 0
    for i in str(n):
        val += int(i)

print(val)