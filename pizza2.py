pizzas = []
pizzas.append('supreme')
pizzas.append('cheese')
pizzas.append('veggie')
friend_pizzas = pizzas[:]
pizzas.append('mushroom')
friend_pizzas.append('black olive')
intro = "My favorite pizzas are: "
friend_intro = "My friend's favorite pizzas are: "
print(intro)
for pizza in pizzas:
	print(pizza.title() + ".")
print(friend_intro)
friend_intro
for fpizza in friend_pizzas:
	print(fpizza.title() + ".")
