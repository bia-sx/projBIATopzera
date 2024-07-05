
dias = ("Domingo","Segunda-Feira","Terca-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sabado")

d = int(input("diga o dia da semana: "))

if 0 < d <= 7:
    print(f"o dia e {dias[d - 1]}")
else: 
    print(" INVALIDO")
