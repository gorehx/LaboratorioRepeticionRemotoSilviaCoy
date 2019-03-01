contadorpar=0;
for n in range(-111100000, 100000000000):
    n=int(input("Ingrese un número"))
    if n%2==0:
        contadorpar=contadorpar+1
    else:
        break
print(contadorpar)