//Crear un procedimiento que calcule la temperatura media de un d�a a partir de la temperatura 
//m�xima y m�nima. Crear un programa principal, que, utilizando un procedimiento, vaya 
//pidiendo la temperatura m�xima y m�nima de n d�as y vaya mostrando la media de cada d�a. El 
//programa pedir� el n�mero de d�as que se van a introducir

Algoritmo Ej_7
	Definir dias, i Como Entero
	Definir max, min Como Real
	Escribir "D�as"
	Leer dias
	Para i<-1 Hasta dias Hacer
		Escribir Sin Saltar "T. Max del d�a: " i
		Leer max
		Escribir Sin Saltar "T. Min del d�a: " i
		Leer min
		Escribir "T.Media del d�a " i " es " tempMedia(max, min)
		Escribir "..........................."
	Fin Para
FinAlgoritmo
SubProceso return <- tempMedia (max, min)
	Definir return Como Real
	return=(max+min)/2
FinSubProceso
