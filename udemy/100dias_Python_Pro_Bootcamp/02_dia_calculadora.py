# En función de la posición
print("Hola"[0]) # H

# Concadenadas
print("123" + "456") # 123456

# Operaciones de valores
print(123 + 456) # 468s

# Enteros largos
print(123_456_789)

# Float
print(3.1415)

#len(12345) dará error ya que este no trabaja con enteros
len("Hola")

# Para comprobar el tipo de dato
print(type("Hola")) # class str (array)

# Para capitalizar de str a int
print(int("123") + int("456")) # 579

# Para redondear números
print(round(3.9)) # 4

# Si quiero concatenar cadena con números 
edad = 12
print(f"Tienes {edad} años")

# PROYECTO 2
print("Bienvenido a mi calculadora!")

monto = float(input("¿Cuál es el monto total? "))
propina = int(input("¿Qué porcentaje quieres dar de propina? 10, 12, 15 "))
comensales = int(input("¿Cuántas personas participan en la propina? "))

porcentaje_propina = propina / 100
total_propina = monto * porcentaje_propina
total_monto = monto + total_propina
porPersona = total_monto / comensales
final = round(porPersona, 2)
print(f"Cada uno deberá de pagar {final} euros")