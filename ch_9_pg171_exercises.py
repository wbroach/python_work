
#~ ### Exercise 9-4
#~ class Restaurant():
    #~ """A simple attempt to model a restaurant."""
    
    #~ def __init__(self, name, cuisine):
        #~ self.name = name
        #~ self.cuisine = cuisine
        #~ self.number_served = 0
            
    #~ def describe_restaurant(self):
        #~ print("The name of the restaurant is " + self.name.title() + 
        #~ " and the restaurant serves " + self.cuisine.title() + " food.")
        
    #~ def open_restaurant(self):
        #~ print(self.name.title() + " is open for business!")
    
    #~ def set_number_served(self, customers_served):
        #~ self.number_served = customers_served
        
    #~ def increment_number_served(self, customers_served):
        #~ self.number_served += customers_served
        
    #~ def read_number_served(self):
        #~ print("This restaurant has served " + str(self.number_served) + " customers.")
        
#~ restaurant = Restaurant('chilis', 'fast-casual crap')

#~ restaurant.set_number_served(23)
#~ restaurant.read_number_served()

#~ restaurant.increment_number_served(7)
#~ restaurant.read_number_served()

### Exercise 9-5
class User():
    """Class model for a website user"""
    
    def __init__(self, first_name, last_name, location, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.sex = sex
        self.login_attempts = 0
        
    def describe_user(self):
        print("\nUser information is as follows: ")
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Location: " + self.location.title())
        print("Sex: " + self.sex.title())
        
    def greet_user(self): 
        full_name = self.first_name.title() + " " + self.last_name.title()
        print("\nHello, " + full_name + "!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
    def read_login_attempts(self):
        if self.login_attempts > 1 or self.login_attempts == 0:
            print("User has attempted to log in " + str(self.login_attempts) + " times.")
        else:
            print("User has attempted to log in " + str(self.login_attempts) + " time.")

user1 = User('will', 'broach', 'athens', 'male')
user1.increment_login_attempts()
user1.read_login_attempts()
user1.increment_login_attempts()
user1.read_login_attempts()
user1.increment_login_attempts()
user1.read_login_attempts()
user1.reset_login_attempts()
user1.read_login_attempts()
