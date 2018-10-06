# Condicionales

# Operadores lógicos
# and	Y
# or	O
# not	NO

# Operadores de comparación o relacionales
# <	Menor que
# >	Mayor que
# <=	Menor o igual que
# >=	Mayor o igual que
# ==	Igual a
# !=	Distinto de

edad = 18
peso = 54.15

if edad > 18:
    print('mayor de edad')
else:
    print('menor de edad')

if edad == 18 and peso >= 54.15:
    print('tienes 18 y pesas 54.15 o mas')

if edad == 18 or edad == 19:
    print("edad correcta")

if edad > 18:
    print('cumple con la edad')
    if peso > 54:
        print('cumple con el peso')
