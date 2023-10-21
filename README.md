# Reto_8
# Punto 1
```python
for num in range(1, 101):
  x = num ** 2
  print(f"{num}, {x}")
```
# Punto 2
```python
# Punto 2
for num in range(1, 999):

  if num % 2 != 0:
    print(num)
for num2 in range(1, 1000):
  if num2 % 2 == 0:
    print(num2)

```
# Punto 3
```python
x = int(input("Ingrese un numero: "))
for x in range(x,1,-1):
  if x%2 == 0:
  
    print(x)
```
# Punto 4
```python
x = int(input("Ingrese un numero: "))

def fact(n):
  if n<0:
    return "ERROR"
  if n==0 or n==1:
    return 1
  for i in range(1,n):
    n=n*i
  return n

for x in range(1,x+1):
  print(f"{x}!= {fact(x)}")
```
# Punto 5
```python
n = int(input("Ingrese un numero: "))
potencia : int = 1
for i in range(1, n+1):
  potencia *= 2
  
print(potencia)
```
# Punto 6
```python
def (n:float, x:int):
  ResultadoPotencia : int = 1
  for i in range(1,n+1):
    ResultadoPotencia *= x
  print(f"{x}^{n}={ResultadoPotencia}")

n = int(input("Ingrese un numero natural: "))
x = float(input("Ingrese un numero real: "))

P(n,x)
```
# Punto 7
```python
def t(n:int):
  print("Tabla de Multiplicar de " +str(n))
  for i in range(1,11):
    r = n*i
    print(f"{n}x{i}={r}")
  print()

for n in range(1, 11):
  t(n)
```
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
