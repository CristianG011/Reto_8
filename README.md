# Reto_8
# Punto 1
1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```python
#punto 1
for num in range(1, 101):
  x = num ** 2
  print(f"{num}, {x}")
```
# Punto 2
2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
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
3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```python
#punto 3
x = int(input("Ingrese un numero: "))
for x in range(x,1,-1):
  if x%2 == 0:
  
    print(x)
```
# Punto 4
4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
#punto 4
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
5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```python
#punto 5
n = int(input("Ingrese un numero: "))
potencia : int = 1
for i in range(1, n+1):
  potencia *= 2
  
print(potencia)
```
# Punto 6
6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```python
#punto 6
def p(n:float, x:int):
  R : int = 1
  for i in range(1,n+1):
    R *= x
  print(f"{x} elevado a la {n} es igual a: {R}")

n = int(input("Ingrese un numero natural: "))
x = float(input("Ingrese un numero real: "))
p(n, x)

```
# Punto 7
7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```python
#punto 7
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
8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$
```python
#punto 8
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
9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$
```python
#punto 9
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
10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$
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
