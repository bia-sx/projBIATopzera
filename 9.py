"""O gestor de uma rede de shoppings, precisa contratar um
sistema para administrar o estacionamento, a principal função do
sistema é calcularTempo(). Considere o valor mínimo de R$9,00
por hora e R$ 1,50 por hora adicional. O principal argumento da
função é o tempo utilizado em minutos, a função deve retornar o
valor total. Caso o usuário fique no estacionamento por menos de
15 minutos, o tempo utilizado não será cobrado."""
def estacionamento (p1):
    if p1==9:
        print("voce vai pagar o valor origional")
    else:
        print("tera um acrecemo")