### Exercise 9-1
#~ class Restaurant():
    #~ """A simple attempt to model a restaurant."""
    
    #~ def __init__(self, name, cuisine):
        #~ self.name = name
        #~ self.cuisine = cuisine
        
    #~ def describe_restaurant(self):
        #~ print("The name of the restaurant is " + self.name.title() + 
        #~ " and the restaurant serves " + self.cuisine.title() + " food.")
        
    #~ def open_restaurant(self):
        #~ print(self.name.title() + " is open for business!")
        
#~ restaurant = Restaurant('chilis', 'fast-casual crap')

#~ print(restaurant.name.title())
#~ print(restaurant.cuisine.title())

#~ restaurant.describe_restaurant()
#~ restaurant.open_restaurant()

### Exercise 9-2

#~ class Restaurant():
    #~ """Creates a restaurant with some other stuff."""
    
    #~ def __init__(self, name, cuisine):
        #~ self.name = name
        #~ self.cuisine = cuisine
        
    #~ def describe_restaurant(self):
        #~ print("The name of the restaurant is " + self.name.title() + 
        #~ " and the restaurant serves " + self.cuisine.title() + " food.")
    
    #~ def open_restaurant(self):
        #~ print(self.name.title() + " is open for business!")


#~ restaurant_crap = Restaurant('the grill', 'drunk food')
#~ restaurant_good = Restaurant('DP dough', 'calzones')
#~ restaurant_awesome = Restaurant('choo-choo', 'college food')

#~ restaurant_crap.describe_restaurant()
#~ restaurant_good.describe_restaurant()
#~ restaurant_awesome.describe_restaurant()  

class User():
    """Class model for a website user"""
    
    def __init__(self, first_name, last_name, location, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.sex = sex
        
    def describe_user(self):
        print("\nUser information is as follows: ")
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Location: " + self.location.title())
        print("Sex: " + self.sex.title())
        
    def greet_user(self): 
        self.full_name = self.first_name.title() + " " + self.last_name.title()
        print("\nHello, " + self.full_name + "!")
        
user1 = User('will', 'broach', 'athens', 'male')
user2 = User('julia', 'butler-mayes', 'athens', 'female')
user3 = User('bryan', 'broach', 'augusta', 'male')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
