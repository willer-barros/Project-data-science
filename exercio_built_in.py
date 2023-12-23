notas = {'trimestre1': 4, 'trimestre2': 6.4, 'trimestre3': 7.5}

somatrio = sum(notas.values())

media = somatrio / len(notas.values())
media = round(media, 1)
print(media)