def make_pizza(size, *toppings):
    """ Summarize the pizza making process """
    if len(toppings) == 1:
        print("\nMaking a " + str(size) + "-inch pizza with the following item: ")
    else:
        print("\nMaking a " + str(size) + "-inch pizza with the following items: ")
    
    for topping in toppings:
        print("\t- " + topping)
    
make_pizza(12, 'pepperoni', 'beer', 'sausage')
make_pizza(14, 'cheese')
