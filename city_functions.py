def get_formatted_city_name(city, country, population=''):
    if population:
        full_name = city + ', ' + country + ' - ' + 'population: ' 
        full_name += str(population)
    else:
        full_name = city + ', ' + country
    
    return full_name.title()
    
    
