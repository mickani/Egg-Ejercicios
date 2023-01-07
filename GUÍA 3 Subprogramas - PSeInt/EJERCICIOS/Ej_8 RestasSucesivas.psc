//Realizar un procedimiento que permita realizar la divisi�n entre dos n�meros y muestre el 
//cociente y el resto utilizando el m�todo de restas sucesivas.
//El m�todo de divisi�n por restas sucesivas consiste en restar el dividendo con el divisor hasta 
//obtener un resultado menor que el divisor, este resultado es el residuo, y el n�mero de restas 
//realizadas es el cociente. Por ejemplo: 50 / 13:
//		50 - 13 = 37 una resta realizada
//		37 - 13 = 24 dos restas realizadas
//		24 - 13 = 11 tres restas realizadas
//	dado que 11 es menor que 13, entonces: el residuo es 11 y el cociente es 3.

Algoritmo Ej_8
	Definir num1, num2 Como Entero
	Escribir Sin Saltar "Num 1: "
	Leer num1
	Escribir Sin Saltar "Num 2: "
	Leer num2
	Escribir restasSucesivas(num1, num2)
FinAlgoritmo
SubProceso resultado <- restasSucesivas(dividento, divisor)
	Definir resultado, cont, resta Como Entero
	resultado=dividento
	cont=0
	Mientras resultado > divisor Hacer
		resta= resultado - divisor
		resultado=resta
		cont=cont + 1
	Fin Mientras
	Escribir "El resto es " resultado " y el cociente es " cont
FinSubProceso
