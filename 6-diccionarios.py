# Diccionarios

twitters = {
    'tavo': '@tavo_jmnz',
    'un_informatico': '@un_informatico'
}

print(twitters)

# agregando datos
twitters['hacktabasco'] = '@hacktabasco'
twitters.update({'codecamp': '@codecamp'})

print(twitters)

# acceder a los elementos
print(twitters['tavo'])
print(twitters.get('tavo'))

# contando elementos
print(len(twitters))