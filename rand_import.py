from random import randint

class Die():
    """Represents a single dice."""
    def __init__(self, sides=6):
        self.sides = sides
        
    def show_sides(self):
        message = "This die has " + str(self.sides) + " sides."
        return message
        
    def roll_die(self):
        result = randint(1, self.sides)
        print("The dice rolled a " + str(result) + ".")


my_dice = Die()
print(my_dice.show_sides())
roll_count = 0
while roll_count < 10:
    
    my_dice.roll_die()
    roll_count += 1

my_dice.sides = 10
print(my_dice.show_sides())
roll_count = 0
while roll_count < 10:
    
    my_dice.roll_die()
    roll_count += 1

my_dice.sides = 20
print(my_dice.show_sides())
roll_count = 0
while roll_count < 10:
    
    my_dice.roll_die()
    roll_count += 1

