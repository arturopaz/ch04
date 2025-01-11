pizzas = ['pepperoni','american','hawaiian']
friend_pizzas = pizzas[:] # Copia de pizza

pizzas.append('spanish') # Agredando nueva pizza a la lista original
friend_pizzas.append('Mediterranean') # Agregando nueva pizza a lista pizza_amigo.

print("Mis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza)

print("\nLas pizzas favoritas de mi amigo son:")
for pizza in friend_pizzas:
    print(pizza)