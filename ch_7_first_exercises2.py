prompt = "\nHow old are you in years?"
prompt += "\n(Enter 'quit' in order to leave the program) "
active = True

while active:
    age_value = input(prompt)
    
    if age_value == 'quit':
        active = False
        
    else:
        age_value = int(age_value)
        if age_value < 3:
            print("Your ticket is free!")
        elif age_value <= 12:
            print("Your ticket costs $10.")
        elif age_value > 12:
            print("Your ticket costs $15.")
    

