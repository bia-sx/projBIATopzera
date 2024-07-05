"""Construa uma função que receba uma string como parâmetro e devolva outra string com os
caracteres embaralhados. Por exemplo: se função receber a palavra python, pode
retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize
em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa,
independentemente de como foram digitados"""
import random

def embaralhar_string(s):
  
    s = s.lower()
    
    caracteres = list(s)
  
    random.shuffle(caracteres)
   
    string_embaralhada = ''.join(caracteres)
    return string_embaralhada


string_original = "Python"
string_embaralhada = embaralhar_string(string_original)
print(f"Original: {string_original}")
print(f"Embaralhada: {string_embaralhada}")
