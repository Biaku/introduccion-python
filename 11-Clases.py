class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def atacar(self):
        print('Atacando')


pj = Personaje('Luffy')

print(pj.nombre)
