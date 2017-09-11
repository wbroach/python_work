from car import Car

class ElectricCar(Car):
    """Makes a child class of Car called ElectricCar."""
    
    def __init__(self, make, model, year):
        """"Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery.battery_size == 70:
            range = 240
        elif self.battery.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
        
class Battery():
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
        else:
            print("This battery is already at the maximum limit.")

