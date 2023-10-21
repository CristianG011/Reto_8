def p(n:float, x:int):
  R : int = 1
  for i in range(1,n+1):
    R *= x
  print(f"{x} elevado a la {n} es igual a: {R}")

n = int(input("Ingrese un numero natural: "))
x = float(input("Ingrese un numero real: "))
p(n, x)

