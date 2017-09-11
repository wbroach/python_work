import json

file_name = 'favorite_number.json'

with open(file_name) as f_obj: 
    fav_number = json.load(f_obj)
    
print("I know your favorite number. It's " + fav_number + "!")
