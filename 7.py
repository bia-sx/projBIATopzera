"""Considere a carga
horária de 40h por semana como salário base, caso
ultrapasse o limite de 40h, o funcionário deve receber
50% a mais por hora excedente."""

def cansaso(p1):
    p1=40
    horas= (p1^50)/100
    if p1 == 40 :
        print("vai ser o mesmo ")
    else:
        print(f"ira ganhar{horas}")
