//Realizar un programa que rellene un vector de tama�o N, con valores ingresados por el 
//usuario. A continuaci�n, se deber� crear una funci�n que reciba el vector y devuelva el valor 
//m�s grande del vector
Algoritmo Ej_5_valorMax
	Definir vector, n, v, i Como entero
	Escribir Sin Saltar "Elija tama�o del vector: "
	Leer n
	Dimension vector[n] 
	Para i<-0 Hasta n-1 Hacer
		Escribir "Valor para sub�ndice: " i
		Leer vector[i]
	FinPara
	Escribir "El valor max. del vector es: " valorMax(vector, n)
FinAlgoritmo
Funcion r <- valorMax ( vector Por Referencia, n Por Referencia )
	Definir r, i, x,mayor Como Entero
	r=0
	Para i<-0 Hasta n-1 Hacer
		si vector[i]>r Entonces
			r=vector[i]
		FinSi
	FinPara
Fin Funcion
