//Un colegio desea saber qu� porcentaje de ni�os y qu� porcentaje de ni�as hay en el curso 
//actual. Dise�ar un algoritmo para este prop�sito. Recuerda que para calcular el porcentaje 
//			puedes hacer una regla de 3 simple. El programa debe solicitar al usuario que ingrese la 
//			cantidad total de ni�os, y la cantidad total de ni�as que hay en el curso. 

Algoritmo ext1PorcentajeBoysGirls
	Definir boys, girls, suma Como Entero
	Definir porcentajeGirls, porcentajeBoys Como Real
	Escribir "Total chicos: " Sin Saltar
	Leer boys
	Escribir "Total chicas: " Sin Saltar
	Leer girls
	suma=girls+boys
	porcentajeGirls=suma*girls/100
	porcentajeBoys=suma*boys/100
	
	Escribir "Porcentaje de ni�os: " porcentajeBoys "%"
	Escribir "Porcentaje de ni�as: " porcentajeGirls "%"
FinAlgoritmo
