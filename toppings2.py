available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
    'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
final_toppings = []

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
        final_toppings.append(requested_topping)
    else:
        print("Sorry, we are out of " + requested_topping + ".")
print("\nFinished making your pizza!\n")


print('The toppings on this pizza are:')

for final_topping in final_toppings:
    print('\t' + final_topping.title())
