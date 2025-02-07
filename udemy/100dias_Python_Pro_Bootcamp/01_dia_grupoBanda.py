print("¡Hola Mundo!") 
print("¡Hola Mundo!\n¡Hola Mundo!\n¡Hola Mundo!\n") 
print("¡Hola Mundo"+ " " + "Sofia!") # son muy importantes los espacios tanto dentro como fuera de la cadena

input("¿Cuál es tu nombre?: ") # para meter tu nombre normal

print("Hola " + input("¿Cuál es tu nombre?: ")) # para meter tu nombre junto con un print

# A comparación de C, no hace falta declarar qué tipo de variable quieres, python lo hace automático
name = input("¿Cuál es tu nombre?: ") # para meter tu nombre normal dentro de la variable name
print(name)

# Para que nos cuente la longuitud de la cadena de caracteres
print(len(input("¿Cuál es tu nombre?: "))) 

# Encadenar variables entre ellas
nombre = input("¿Cuál es tu nombre?: ") 
longitud = len(nombre)
print(longitud)

# PROYECTO 1
print("Bienvenido al generador de nombres de bandas")
city = input("¿En qué ciudad creciste?: \n")
pet = input("¿Cuál es el nombre de tu mascota?: \n")
print("El nombre de tu banda es: " + " " + city + " " + pet)