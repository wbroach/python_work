import pizza

pizza.make_pizza(12, 'pepperoni', 'beer', 'sausage')
pizza.make_pizza(14, 'cheese')

from pizza import make_pizza

make_pizza(12, 'pepperoni', 'beer', 'sausage')
make_pizza(14, 'cheese')

from pizza import make_pizza as mp

mp(12, 'pepperoni', 'beer', 'sausage')
mp(14, 'cheese')
