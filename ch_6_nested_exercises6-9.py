favorite_places = {
    'julia': ['athens', 'la jolla', 'the lake'],
    'nancy': ['athens', 'london', "ed's house"],
    'will': ['ecuador', 'winder', 'liquor store'],
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s " + "favorite places are:")

    for place in places:
        print(place.title())
