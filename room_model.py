from random import choice


class Room():
    """Models the room"""
    
    def __init__(self):
        self.x_squares = 8
        self.y_squares = 8
        self.exit_square_x = self.x_squares
        self.exit_square_y = self.y_squares
        self.bot_starting_x_point = choice([value for value in range(0, self.x_squares)]) 
        self.bot_starting_y_point = choice([value for value in range(0, self.y_squares)])
        self.bot_current_x_point = self.bot_starting_x_point
        self.bot_current_y_point = self.bot_starting_y_point
        self.wall_x_left_location = choice([value for value in range(0, self.x_squares)])
        self.wall_x_right_location = self.wall_x_left_location + choice([value for value in range((self.wall_x_left_location + 1)])), self.x_squares)]
        #~ self.wall_y_plane = choice([value for value in range(0, self.y_squares)])
        
    #~ def move_biobot(self):
        #~ """Models robot movement. Limited to moving N or E"""
        #~ x_step = "X"
        #~ y_step = "Y"
        #~ step_direction = choice([x_step, y_step])  
        #~ if step_direction == "X":
            #~ self.bot_current_x_point += 1
        #~ elif step_direction == "Y":
            #~ self.bot_current_y_point += 1
