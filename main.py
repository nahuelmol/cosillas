
def calculator():

	mycadena = [65,6,5]
	cont = 0
	aux = 0 
	for i in mycadena:
		if cont != 0:
			aux = mycadena[cont - 1] / i 
			mycadena[cont] = aux
		cont = cont + 1

	print(aux)
if __name__ == "__main__":
	calculator()