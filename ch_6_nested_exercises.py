girlfriend = {
    'first name': 'julia',
    'last name': 'butler-mayes', 
    'age': 31, 
    'city': 'athens',
        }

girlfriend_mom = {
    'first name': 'nancy',
    'last name': 'butler',
    'age': 59,
    'city': 'la jolla',
    }
    
girlfriend_brother = {
    'first name': 'colin',
    'last name': 'butler-mayes',
    'age': 26,
    'city': 'alpharetta',
    }
    
girlfriend_family_members = []
girlfriend_family_members.append(girlfriend)
girlfriend_family_members.append(girlfriend_mom)
girlfriend_family_members.append(girlfriend_brother)

for member in girlfriend_family_members:
    full_name = member['first name'].title() + " " + member['last name'].title()
    print("\n" + full_name + "'s" + " information is as follows:")
    print("Age: " + str(member['age']))
    print("City: " + member['city'].title())
