requested_toppings = ['mushrooms', 'onions', 'pineapple']

#if requested_topping != 'anchovies':
    #print("Hold the anchovies!")
#else:
    #print("Bring on the anchovies!")
for topping in requested_toppings:
    if topping == 'mushrooms' or topping == 'onions':
        print("It's got mushrooms")
    else:
        print("It's not in the list")

