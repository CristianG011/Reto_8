#Punto 9
import math
def f(i: int):
    if i == 0:
        return 1
    else:
        p = 1
        for numero in range(1, i + 1):
            p *= numero
        return p
a = int(input("Ingrese número de iteraciones: "))
x = float(input("Ingrese valor x en radianes: "))

suma : float = 0
for s in range(a + 1):
    d = (x ** (2 * s + 1)) / f(2 * s + 1)
    d *= (-1) ** s
    suma += d


print(f"{suma}")
print(f"{math.sin(x)}")
z = (abs(suma - math.sin(x))/math.sin(x))*100
print(f"El porcentaje de error es de {z}")