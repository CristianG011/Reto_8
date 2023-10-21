import math
a = int(input("Ingrese número de iteraciones: "))
x = float(input("Ingrese valor x en radianes: "))
suma = 0
for s in range(a + 1):
    d = (x ** (2 * s + 1)) / (2 * s + 1)
    d *= (-1) ** s
    suma += d
print(f"{suma}")
print(f"{math.atan(x)}")
z = (abs(suma - math.atan(x))/math.atan(x))*100
print(f"El porcentaje de error es de {z}")
