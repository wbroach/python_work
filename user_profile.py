def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything we know about a user."""
    dict = {}
    dict['first'] = first
    dict['last'] = last
    for key, value in user_info.items():
        dict[key] = value
    return dict

def print_profile(dict):
    for key, value in dict.items():
        print(key.title() + ": " + str(value).title())

    
julia_profile = build_profile('julia', 'butler-mayes', age = 31, location = 'athens')
print_profile(julia_profile)



    
    
