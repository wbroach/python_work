belle = {
    'name': 'belle',
    'type': 'dog',
    'owner': 'will',
    }
simon = {
    'name': 'simon',
    'type': 'cat',
    'owner': 'nancy',
    }
toby = {
    'name': 'toby',
    'type': 'maine coon',
    'owner': 'julia',
    }

pets = []
pets.append(belle)
pets.append(simon)
pets.append(toby)

for pet in pets:
    print("\nThe information on this pet is as follows:")
    print("Name: " + pet['name'].title())
    print("Type: " + pet['type'].title())
    print("Owner: " + pet['owner'].title())
