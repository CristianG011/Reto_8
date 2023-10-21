# Reto_8
# Punto 8
```python
#Punto 8
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
```

# Punto 9
```python
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
```
# Punto 10
```python
# Punto 10
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
```
