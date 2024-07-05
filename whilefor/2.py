while True:
  b1 = float(input("Digite a base menor: "))
  b2 = float(input("Digite a base maior: "))
al = float(input("Digite a altura: "))

if 0 > b1 or 0 > b2 or 0 > al:
    print("VALORES INVÁLIDOS")
else: 
    area = (b1 + b2) * al / 2
    print("A área do trapézio é", area)