from random import choice


class Room():
    """Models the room"""
    def __init__(self, x_squares=8, y_squares=8)
        self.x_squares = x_squares
        self.y_squares = y_squares
        self.Walls = Walls()
        self.BioBot = BioBot()
        self.exit_square_x = x_squares
        self.exit_square_y = y_squares
        
class BioBot():
    """A class representing a biobot."""
    def __init__(self):
        """Initialize the robot."""
        # Walk starts at a random point
        self.starting_x_point = choice([value for value in range(0, Room.x_squares)])
        self.starting_y_point = choice([value for value in range(0, Room.y_squares)])
        self.current_x_point = self.starting_x_point
        self.current_y_point = self.starting_y_point
        
    def move_biobot(self):
        """Models robot movement. Limited to moving N or E"""
        x_step = "X"
        y_step = "Y"
        step_direction = choice([x_step, y_step])  
        if step_direction == "X":
            self.current_x_point += 1
        elif step_direction == "Y":
            self.current_y_point += 1
            
    def biobot_stuck(self):
        
        
class Walls():
    """A class representing the walls in the room."""
    def __init__(self):
        self.x_left_location = choice([value for value in range(0, Room.x_squares)])
        self.x_right_location = self.x_left_location + choice([value for value in range((self.x_left_location + 1), Room.x_squares)])
        self.y_plane = choice([value for value in range(0, Room.y_squares)])
        
        
    
        
