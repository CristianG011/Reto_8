def t(n:int):
  print("Tabla de Multiplicar de " +str(n))
  for i in range(1,11):
    r = n*i
    print(f"{n}x{i}={r}")
  print()

for n in range(1, 11):
  t(n)