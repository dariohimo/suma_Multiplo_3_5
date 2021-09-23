suma_tres_cinco = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
       suma_tres_cinco += i
       print(f" {i:>3}")
               
       
print(f"\n Total de la suma Números Pares de 3 y 5 es: {suma_tres_cinco:,}")
