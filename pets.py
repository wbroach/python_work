#~ def describe_pet(pet_name, animal_type = 'dog'):
    #~ print("\nI have a " + animal_type + ".")
    #~ print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
#~ describe_pet(pet_name = 'belle')
#~ describe_pet(animal_type = 'hamster', pet_name = 'harry')

#### new exercise

#~ def make_shirt(size = 'large', shirt_message = 'I love Python'):
    #~ print("\nThe size of the ordered shirt is " + size + ".")
    #~ print("The message on the " + size + " shirt is " + '"' + shirt_message + '."')
    
#~ make_shirt()
#~ make_shirt('medium',)
#~ make_shirt(shirt_message = 'I love beer')


#### new exercise
def describe_city(city, country = 'united states'):
    print(city.title() + " is in " + country.title() + ".\n")
    
describe_city('atlanta')
describe_city(city = 'winder')
describe_city('athens', country = 'greece')

