#~ prompt = "\nPlease enter a topping of your choice:"
#~ prompt +="\n(Enter 'quit' to finish entering toppings). "

#~ active = True

#~ while True:
    #~ message = input(prompt)
    #~ if message == 'quit':
        #~ break
    #~ else:
        #~ print(message)

### NEXT EXERCISE

prompt = "\nHow old are you in years?"
prompt += "\n(Enter 'quit' in order to leave the program) "

while True:
    age_value = input(prompt)
    
    if age_value == 'quit':
        break
    else:
        age_value = int(age_value)
        
        if age_value < 3:
            print("Your ticket is free!")
        elif age_value <= 12:
            print("Your ticket costs $10.")
        elif age_value > 12:
            print("Your ticket costs $15.")
        
