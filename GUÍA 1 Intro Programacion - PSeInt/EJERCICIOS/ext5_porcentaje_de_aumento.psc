//Crear un programa que solicite al usuario que ingrese el precio de un producto al inicio del 
//a�o, y el precio del mismo producto al finalizar el a�o. El programa debe calcular cu�l fue el 
//porcentaje de aumento que tuvo ese producto en el a�o y mostrarlo por pantalla.
Algoritmo ext5_porcentaje_de_aumento
	Definir precio1, precio2, resta, aumento Como Real
	Escribir "Precio producto inicio del a�o"
	Leer precio1
	Escribir "Precio producto fin de a�o"
	Leer precio2
	resta=precio2 - precio1
	aumento=resta/precio1*100
	Escribir "Porcentaje de aumemto: " aumento "%"
FinAlgoritmo
