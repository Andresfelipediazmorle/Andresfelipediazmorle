h = int(input("\nIngrese un numero entero positivo: "))  # h numero entero positivo mayor que cero
count = 0
# Numeros primos son solo divisibles(exactamente) por 1 y el mismo numero

def Primos(h,count):
    "Si el numero h tiene mas de dos divisiones exactas no es primo"
    for i in range(1,h+1,1):
        if h%i == 0: 
            count +=1
    if count == 2: # Si count es igual a 2 pues el numero h es primo
        return True
    else:        
        return False

Si = Primos(h,count)

if bool(Si) == True:
    print("\nEl numero " + str(h) + " es primo")
else:
    print("\nEl número " +str(h) + " no es primo" )        