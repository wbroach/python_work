cities = {
    'new york': {
        'country': 'USA',
        'population': 11000000,
        'fact': 'financial center of the world',
        },
    'atlanta': {
        'country': 'CSA',
        'population': 8000000,
        'fact': 'empire city of the south',
        },
    'athens': {
        'country': 'GA',
        'population': 100000,
        'fact': 'UGA is located here',
        },
    }
        
for city, city_info in cities.items():
    country_located = city_info['country']
    population_data = city_info['population']
    fun_fact = city_info['fact']
    
    print("\nData for " + city.title() + " is as follows:")
    print("Country: " + country_located.upper())
    print("Population: " + str(population_data))
    print("Interesting factoid: " + fun_fact)
    
    
    
    
    
