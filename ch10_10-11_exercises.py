import json

file_name = 'favorite_number.json'

try:
    with open(file_name) as f_obj: 
        fav_number = json.load(f_obj)
except FileNotFoundError:    
    favorite_number = input("Please enter your favorite number: ")
    with open(file_name, 'w') as f_obj:
        json.dump(favorite_number,f_obj)
else:
    print("I know your favorite number. It's " + fav_number + "!")
