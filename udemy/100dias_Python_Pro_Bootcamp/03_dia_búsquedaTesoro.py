# Condicional IF
water = 50
if water > 80:
    print("Demasiado")
elif water <= 80:
    print("Tope")
else:
    print("Sigue llenando")

# Módulo operador (10 % 5 = 2)

# Programa de pedidos de pizza
print("Bienvenidos a los pedidos de pizza de Python")
tamaño = input("¿Tamaño S, M, L?: ")
pepperoni = input("¿Quieres pepperoni? S, N: ")
queso_extra = input("¿Quieres más queso? S, N: ")

bill = 0
if tamaño == "S":
    bill += 15
elif tamaño == "M":
    bill += 20
elif tamaño == "L":
    bill += 25
else:
    print("Selecciona un tamaño obligatoriamente")

if pepperoni == "Y":
    if tamaño == "S":
        bill += 2
    else:
        bill += 3

if queso_extra == "Y":
    bill += 1

print(f"El precio de tu pizza es de {bill}")

""" 
Operadores lógicos:

A and B
True and True = True
True and False = False
False and True = False

C or D
Si o si deben de ser las dos iguales
True and True = True

not E

"""

# PROYECTO DÍA 3
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
''')

print("Bienvenido a mi búsqueda del tesoro con condicionales!")
print("Tu principal misión es conseguir el tesoro seleccionando opciones.")

choice1 = input('Estás en un camino, ¿Quieres ir a la "derecha" o "izquierda"? ').lower()

if choice1 == "izquierda":
    choice2 = input('Te encuentras un río. ¿Decides "nadar" o "esperar" una barca? ').lower()

    if choice2 == "esperar":
        choice3 = input('Has llegado al otro lado de la orilla y ves una casa con 3 puertas. '
                        '¿Cuál eliges: "rojo", "azul" o "amarillo"? ').lower()

        if choice3 == "rojo":
            print("La sala está en llamas, has perdido.")
        elif choice3 == "azul":
            print("Hay un león, has perdido.")
        elif choice3 == "amarillo":
            print("El tesoro está aquí, ¡ganaste!")
        else:
            print("Opción no válida, intenta de nuevo.")

    else:
        print("Te ahogaste en el río, has perdido.")

elif choice1 == "derecha":
    print("Caíste en un pozo, has perdido.")

else:
    print("Opción no válida, intenta de nuevo.")
