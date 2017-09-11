import json


filename = 'user.json'

try:
    with open(filename) as f_obj:
        name_user = json.load(f_obj)
except FileNotFoundError:    
    user_name = input("Please provide your name: ")
    with open(filename, 'w') as f_obj: 
        json.dump(user_name, f_obj)
        print("We'll remember you when you come back, " + user_name + "!")
else:
    print("Hello again, " + name_user + "!")
    

