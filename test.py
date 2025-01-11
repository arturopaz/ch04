my_comida = ['arroz chaufa','arroz con pollo','arroz con chancho','aji de gallina']
comida_amigo = my_comida[:]
print(type(my_comida), id(my_comida))
print(type(comida_amigo), id(comida_amigo))
print('Agrego comida a mi lista...')
my_comida.append('lomito saltado')
print('Agrego comida a la lista de mi amig..')
comida_amigo.append('papa rellena')
print('Mostrando las nuevas listas:\n')
print(f"Mi lista: {my_comida}")
print(f"Amigo lista: {comida_amigo}")
