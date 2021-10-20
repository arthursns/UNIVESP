z = input().split(" ")

a, b = z
a = int(a)
b = int(b)
resto = a % b

while(resto != 0):
    a = b
    b = resto
    MDC = b
    resto = a % b

print("O MDC é " + str(MDC))