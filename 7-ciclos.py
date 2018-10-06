edades = (15, 48, 24, 15)
pesos = [14, 45, 74.1, 33.33]

personaje = {
    'ataque': 15,
    'fuerza': 45,
    'vitalidad': 78,
    'nombre': 'el macho'
}

for numero in range(15):
    print(numero)

print('======================')

for edad in edades:
    print(edad)

print('======================')
for peso in pesos:
    print(peso)

for dato in personaje:
    print(dato)

for key, value in personaje.items():
    print(key, value)

vida = 10

while vida > 0:
    print('vida', vida)
    vida -= 1
