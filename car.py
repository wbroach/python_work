class Car():
    """A class that describes a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns long name/descriptor."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title() 

    def read_odometer(self):
        """Print a statement showing the odometer reading for a car."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
        
#~ class ElectricCar(Car):
    #~ """Makes a child class of Car called ElectricCar."""
    
    #~ def __init__(self, make, model, year):
        #~ """"Initialize attributes of the parent class."""
        #~ super().__init__(make, model, year)
        #~ self.battery = Battery()
        
    #~ def get_range(self):
        #~ """Print a statement about the range this battery provides."""
        #~ if self.battery.battery_size == 70:
            #~ range = 240
        #~ elif self.battery.battery_size == 85:
            #~ range = 270
            
        #~ message = "This car can go approximately " + str(range)
        #~ message += " miles on a full charge."
        #~ print(message)
        
        
#~ class Battery():
    #~ """A simple attempt to model a battery for an electric car."""
    
    #~ def __init__(self, battery_size=70):
        #~ """Initialize the battery's attributes."""
        #~ self.battery_size = battery_size
    
    #~ def describe_battery(self):
        #~ print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    #~ def upgrade_battery(self):
        #~ if self.battery_size == 70:
            #~ self.battery_size = 85
        #~ else:
            #~ print("This battery is already at the maximum limit.")
