//Hacer un algoritmo que lea un n�mero por el teclado y determine si tiene 
//tres d�gitos.

Algoritmo extra7_Tiene_3_digitos
	Definir num Como Caracter
	Definir digitos Como Logico
	Escribir "Num: " Sin Saltar
	Leer num
	digitos=Longitud(num)<3
	Segun num Hacer
		digitos:
			Escribir "Tiene 3 d�gitos"
		NO(digitos):
			Escribir "No tiene 3 d�gitos"
		De Otro Modo:
			Escribir "Error..."
	Fin Segun
FinAlgoritmo
