#~ def make_sandwich(bread, chips, *stuff):
    #~ print("\nMaking your sandwich with " + bread.lower() + " and " + chips + " chips" +
    #~ " and the following toppings:")
    #~ for topping in stuff:
        #~ print("\t- " + topping.title())
        
#~ make_sandwich('wheat', 'potato', 'mayo', 'roast beef')


def build_profile(first, last, **items):
    dict = {}
    dict['first'] = first
    dict['last'] = last
    for key, value in items.items():
        dict[key] = value
    return dict
    
will_profile = build_profile('will', 'broach', age=23, location='athens', bar = 'walkers')
print(will_profile)

def build_car(make, model, **items):
    dict = {}
    dict['make'] = make
    dict['model'] = model
    for key, value in items.items():
        dict[key] = value
    return dict
    
car = build_car('ford', 'taurus', color = 'blue', tow_package = True)
print(car)
