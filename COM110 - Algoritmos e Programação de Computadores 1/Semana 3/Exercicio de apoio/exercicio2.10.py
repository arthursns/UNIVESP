import math

# Escreva expressões Python correspondentes ao seguinte: 
#  (a)O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
a = int(input())
b = int(input())

c = math.sqrt(a**2 + b**2)

print("A hipotenusa é: " + str(c))

#  (b)O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
if (c == 5):
    print("O comprimento acima é 5")
else:
    print("O comprimento acima não é 5")

#  (c)A área de um disco com raio a 
aRaio = int(input())

area = math.pi * (aRaio**2)

print("A área do disco é: " + str(area))

#  (d)O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo com centro (a, b) e raio r
pontoX = int(input())
pontoY = int(input())
centroA = int(input())
centroB = int(input())
raio = int(input())

if (math.sqrt(((pontoX - centroA)**2) + ((pontoY - centroB)**2)) == raio):
    print("O ponto está dentro do círculo")
else:
    print("O ponto não está dentro do círculo")