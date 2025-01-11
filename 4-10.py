grupos = ['queen','led zeppelin','red hot chilli peppers','system of a down','black sabbath','supertramp','pink floyd']

print("Mis artistas favoritos son: ", grupos )
print("Los primeros 3 elementos de la lista son:\n")
for grupo in grupos[:3]:
    print(grupo)

mitad = int(len(grupos)/2)
print("\nEl total de artistas son:", len(grupos))
print("La mitad es:", mitad)

print("\nLos 3 artistas empezando desde la mitad de la lista:")
for grupo in grupos[(mitad-1):mitad+2]:
    print(grupo)


print("\nLos ultimos tres elementos en la lista son:")
for grupo in grupos[-3:]:
    print(grupo)
    



