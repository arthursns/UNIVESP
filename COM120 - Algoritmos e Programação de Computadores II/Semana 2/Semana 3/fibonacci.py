# Exercício da Videoaula 5 onde tenho que fazer um algoritmo que utilize Recursão para o cálculo de Fibonacci

def fibonacci(n):
    if (n == 1) or (n == 0):
        return(n)
    else:
        n = fibonacci(n-1) + fibonacci(n-2)
        return(n)