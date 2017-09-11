### Exercise 9-5
class User():
    """Class model for a website user"""
    
    def __init__(self, first_name, last_name, location, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.sex = sex
        self.login_attempts = 0
        self.privileges = ['can add post', 'can edit post', 
        'cannot delete post', 'cannot ban user']
        
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
            
    def show_privileges(self):
        show_privileges_input = input("Show " + self.first_name.title() + " " 
        + self.last_name.title() + " privileges? (y or n) ")
        
        if show_privileges_input == 'y':
            for i in self.privileges:
                print("\t- " + i.title())

class Admin(User):
    """A subclass of user, models the admin user object and characteristics."""
    
    def __init__(self, first_name, last_name, location, sex):
        super().__init__(first_name, last_name, location, sex)
        #Yep, you can overwrite superclass privileges in a subclass
        self.privileges = ['can add post', 'can edit post', 
        'can delete post', 'can ban user']
        

user1 = User('will', 'broach', 'athens', 'male')
user1.show_privileges()

admin1 = Admin('julia', 'butler-mayers', 'athens', 'female')
admin1.show_privileges()

