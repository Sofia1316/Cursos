#include <stdio.h>
#include <stdlib.h>

/*
Aplicación de calificaciones que automatiza el cálculo de las calificaciones para los alumnos de una clase. 
Parámetros:
	Recibe una breve lista de cuatro alumnos y cinco calificaciones de cada uno.
	Cada calificación se expresa como un valor entero, de 0 a 100, donde 100 representa que está perfecto.
	Las notas finales son el promedio de las notas de las cinco tareas.
	Debe realizar operaciones matemáticas básicas para calcular las calificaciones finales de cada alumno.
	La aplicación debe generar o mostrar el nombre de cada alumno y la nota final.
*/

int main(){
	
// variables iniciales:
 
int currentAssignments = 5;

int sophia1 = 93;
int sophia2 = 87;
int sophia3 = 98;
int sophia4 = 95;
int sophia5 = 100;

int nicolas1 = 80;
int nicolas2 = 83;
int nicolas3 = 82;
int nicolas4 = 88;
int nicolas5 = 85;

int zahirah1 = 84;
int zahirah2 = 96;
int zahirah3 = 73;
int zahirah4 = 85;
int zahirah5 = 79;

int jeong1 = 90;
int jeong2 = 92;
int jeong3 = 98;
int jeong4 = 100;
int jeong5 = 97;

//inicialización de variables en 0:

int sophiaSuma = 0;
int nicolasSuma = 0;
int zahirahSuma = 0;
int jeongSuma = 0;

//suma de notas correspondientes:

	int sophiaSuma1 = sophia1 + sophia2 + sophia3 + sophia4 + sophia5;
	int nicolasSuma2 = nicolas1 + nicolas2 + nicolas3 + nicolas4 + nicolas5;
	int zahirahSuma3 = zahirah1 + zahirah2 + zahirah3 + zahirah4 + zahirah5;
	int jeongSuma4 = jeong1 + jeong2 + jeong3 + jeong4 + jeong5;

//variables visibles al compilar:

printf("Sophia:%d\n", sophiaSuma1);
printf("Nicolas:%d\n", nicolasSuma2);
printf("Zahirah:%d\n", zahirahSuma3);
printf("Jeong:%d\n", jeongSuma4);


return EXIT_SUCCESS;
}
