# Programa que calcula el Minimo Comun Multipo de 2  numeros

print("\nCalculadora del Mínimo Común Múltiplo de dos numeros")
print("Por favor, ingrese los numeros")

n1 = int(input("\n1er Numero: "))
n2 = int(input("2do Numero: "))

def m_c_m(n1, n2) :

	
	if (n1 > n2) == True :
		num_mayor= n1
		num_menor= n2

	if (n1 < n2) == True :
		num_mayor= n2
		num_menor= n1

	while num_menor != 0 :
		p = num_menor
		num_menor= num_mayor % num_menor
		num_mayor= p
		if num_menor == 0 :
			break

	if num_menor == 0 :		
   
		return (n1//num_mayor) * n2     

MCM = m_c_m(n1, n2)
print("\nEl Mínimo Común Múltiplo de " + str(n1) + " y " + str(n2) + " es: " )
print(" MCM = " + str(MCM))


def w():
	t = input("\nSi desea calcular el MCM de nuevo (escriba 2)(si desea salir escriba 1): ")
	while t == "2" :

		def d(t):

			n1 = int(input("\n1er Numero: "))
			n2 = int(input("2do Numero: "))

			m_c_m(n1, n2)
			MCM = m_c_m(n1, n2)
			print("\nEl Mínimo Común Múltiplo de " + str(n1) + " y " + str(n2) + " es: " )
			print(" MCM = " + str(MCM))
	
			w()

		d(t)
			

		break

	if t == str("1") :
	
		return 

w()

