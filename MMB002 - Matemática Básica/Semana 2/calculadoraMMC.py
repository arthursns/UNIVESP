z = input().split(" ")

a, b = z
a = int(a)
valor1 = int(a)
b = int(b)
valor2 = int(b)
resto = a % b
MDC = 1

while(resto != 0):
    a = b
    b = resto
    MDC = b
    resto = a % b

MMC = (valor1 * valor2)/MDC
MMC = int(MMC)
print("O MMC é " + str(MMC))