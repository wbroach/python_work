class Apartment():
    """Create a simple class that models an apartment."""
    
    def __init__(self, complex_name, building_name, apartment_number):
        self.complex_name = complex_name
        self.building_name = building_name
        self.apartment_number = apartment_number
        self.is_clean = False
        
    def show_cleaning_status(self):
        if self.is_clean == False:
            print("\nThis apartment needs to be cleaned.\n")
        else:
            print("\nThis apartment is clean.\n")
            
    def make_apartment_clean(self):
        if self.is_clean == True:
            print("\nThis apartment is already clean!\n")
        else:
            print("\nCleaning the apartment\n")
            self.is_clean = True
            
    def make_full_apt_name(self):
        full_name = self.complex_name + ', ' + self.building_name 
        full_name += ' ' + str(self.apartment_number)
        return full_name.title()




