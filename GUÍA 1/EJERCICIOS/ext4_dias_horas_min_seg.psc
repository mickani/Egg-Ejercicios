//A partir de una conocida cantidad de d�as que el usuario ingresa a trav�s del teclado, escriba 
//un programa para convertir los d�as en horas, en minutos y en segundos.
Algoritmo ext4_dias_horas_min_seg
	Definir dias, hora, minutos, seg Como real
	Escribir "D�a/s: " Sin Saltar
	Leer dias
	hora=dias*24
	minutos=dias*1440
	seg=dias*86400
	Escribir dias " d�as son: "
	Escribir hora "hs"
	Escribir minutos "min"
	Escribir seg "seg"  

FinAlgoritmo
