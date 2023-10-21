import math
a = int(input("Ingrese número de iteraciones "))
x = float(input("Ingrese valor b "))
def factorial(i:int):
    if i == 0:
        return 1
    else:
        p = 1
        for n in range(1,i+1):
            p *= n
        return p
suma : float = 0

for s in range(0,a+1):
    d = x**s
    d = d/factorial(s)
    suma += d
print(suma)
print(math.e ** x)
import math
z = (abs(suma - math.e ** x)/math.e ** x) * 100
print(f"El posentaje de error es de {z}")