### Exercise 9-6
class Restaurant():
    """A simple attempt to model a restaurant."""
    
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
            
    def describe_restaurant(self):
        print("The name of the restaurant is " + self.name.title() + 
        " and the restaurant serves " + self.cuisine.title() + " food.")
        
    def open_restaurant(self):
        print(self.name.title() + " is open for business!")
    
    def set_number_served(self, customers_served):
        self.number_served = customers_served
        
    def increment_number_served(self, customers_served):
        self.number_served += customers_served
        
    def read_number_served(self):
        print("This restaurant has served " + str(self.number_served) + " customers.")


class IceCreamStand(Restaurant):
    """A subclass of Restaurant. A simple model for an ice cream stand."""
    
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'strawberry', 'peanut butter', 'egg nog']
        
    def show_flavors(self):
        print("\nThis ice cream stand serves the following flavors:")
        
        for i in self.flavors:
            print("\t- " + i.title())
        
#~ restaurant = Restaurant('chilis', 'fast-casual crap')

#~ restaurant.set_number_served(23)
#~ restaurant.read_number_served()

#~ restaurant.increment_number_served(7)
#~ restaurant.read_number_served()

ice_cream_stand = IceCreamStand('Bootys ', 'soft-serve')

ice_cream_stand.show_flavors()
ice_cream_stand.increment_number_served(15)
ice_cream_stand.read_number_served()

